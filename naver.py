#네이버 뉴스 속보 기사 스크래핑

import requests
from bs4 import BeautifulSoup

LIMIT = 1
URL = f"https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001"


#한 페이지당 마지막 페이지를 불러옴
def get_last_page():
    result = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})

    #BeautifulSoup(html_doc, "html.parser")
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div",{"class":"paging"})
    pagination = list(pagination)
    pages = []
    for page in list(pagination):
        if page != '\n':
            pages.append(page.string)
    pages = pages[:-1]
    i = 0
    for page_num in pages:
        page_num = int(page_num)
        pages[i] = page_num
        i+=1
    max_page = pages[-1]
    return max_page

get_last_page()