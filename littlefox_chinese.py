# 참고 사이트 : https://www.lightsky.kr/144
# 주소에서 en, ko만 변경해서 사용하면 됨
# 작성일 : 2021.12

import requests
from bs4 import BeautifulSoup as BS
import re


def text_prepro(text):
    text = re.sub("\n", " ", text)
    text = re.sub("\r", "", text)
    text = re.sub("\t", "", text)
    return text


#html페이지가 아닌 로그인을 처리하는 페이지 주소를 입력 -> F12(개발자모드)-Network에서 확인
#https://chinese.littlefox.com/ko/login/script_proc
login_url = "https://chinese.littlefox.com/en/login/auth_process"

session = requests.session()

# 해당 사이트의 로그인 정보를 dict변수에 입력
# 변수이름('loginid', 'loginpw') -> F12(개발자모드)-Network에서 확인
params = dict()
params['loginid'] = 'kyullzzang@gmail.com'
params['loginpw'] = 'Foaldks121'

res = session.post(login_url, data=params)
res.raise_for_status()

# http의 header와 cookie값으로 넘어가는 값을 출력해봄
# print(res.headers)
# print(session.cookies.get_dict())


src = []
trg = []
tmp = []

for i in range(0, 10000):
    try:
        j = str(i).zfill(4)
        # 로그인 후 크롤링할 주소를 입력
        crawl_url = "https://chinese.littlefox.com/en/supplement/org/C000"+j

        res = session.get(crawl_url)
        soup = BS(res.content, 'html.parser')

        for text_extract in soup.find_all('div', class_='t0 text_size simsun'):
            ex_sent = text_extract.text.lstrip()
            ex_sent = text_prepro(ex_sent)
            src.append(ex_sent)

        for text_extract2 in soup.find_all('div', class_='t2 text_size'):
            ex_sent2 = text_extract2.text.lstrip()
            ex_sent2 = text_prepro(ex_sent2)
            trg.append(ex_sent2)

    except Exception as e:
        print("There's no page.")




idx = []
save_path = "D:/Data/Corpus/MEDIA/littlefox_chinese/"

if len(src) == len(trg):
    for k in range(0, len(src)):
        src_text = src[k]
        trg_text = trg[k]
        if len(src_text) < 2 or len(trg_text) < 2:
            continue
        else:
            idx.append(k)

    with open(save_path + 'zh.txt', 'w', -1, 'utf-8') as output1:
        with open(save_path + 'en.txt', 'w', -1, 'utf-8') as output2:
            for j in idx:
                output1.write(src[j]+"\n")
                output2.write(trg[j]+"\n")
        output2.close()
    output1.close()

else:
    with open(save_path + 'zh.txt', 'w', -1, 'utf-8') as output:
        for line in src:
            output.write(line + "\n")
    output.close()

    with open(save_path + 'en.txt', 'w', -1, 'utf-8') as output:
        for line in trg:
            output.write(line + "\n")
    output.close()
    
