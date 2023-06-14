
import wikipediaapi


lanlist = ['ko', 'en']

wiki=wikipediaapi.Wikipedia('ko')

page_word = wiki.page('대한민국의 인터넷 신조어 목록')
print("Page - Exist: %s" %page_word.exists())

wiki = wikipediaapi.Wikipedia(language='ko',
                              extract_format=wikipediaapi.ExtractFormat.WIKI)

s_page = wiki.page("대한민국의 인터넷 신조어 목록")
page_text = s_page.text

with open("crawltest.txt", "w", -1, 'utf-8') as output:
    output.write(page_text)