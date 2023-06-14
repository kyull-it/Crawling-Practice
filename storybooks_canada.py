# 작성일 : 2021.12

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def text_prepro(text):
    text = re.sub("\n", " ", text)
    return text


#zh = mandarin (북경어 : 북경표준어)
lan_lst = ["en", "am", "bn", "fr", "ar", "de", "yue", "fa", "it", "ko", "zh", "es", "pt", "pl", "pa", "so", "sw", "tl", "tr", "ur"]
path = "D:/Data/Corpus/MEDIA/storybooks_canada/"


for k in range(1, 501):
    print(k)

    for lan in lan_lst:
        print(lan)

        try:
            k = str(k).zfill(4)
            html = urlopen("https://www.storybookscanada.ca/stories/"+lan+"/"+k+"/")
            bshtml = BeautifulSoup(html, 'html.parser')
            # print(bshtml.body.prettify())

            for i in range(1,6):

                try:
                    j = str(i)
                    lst = []
                    text_extract = bshtml.find_all('div', class_='column col-6 col-lg-11 col-md-12 col-sm-12 level'+j+'-txt def')
                    for div in text_extract:
                        h3_text = div.text.strip()
                        h3_text = text_prepro(h3_text)
                        lst.append(h3_text+"\n")

                    if not lst:
                        continue
                    else:
                        print(lst)
                        with open(path + lan + "_" + k + "." + lan, 'w', -1, 'utf-8') as output:
                            for i, idx in enumerate(lst):
                                # print(str(i) + " : " + idx)
                                output.write(idx)
                        output.close()

                except Exception as e:
                    continue

        except Exception as ex:
            continue

    print("end : ", k)
