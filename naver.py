#네이버 뉴스 속보 기사 스크래핑

import requests
from bs4 import BeautifulSoup

LIMIT = 1
URL = f"https://news.naver.com/main/list.nhn?mode=LSD&sid1=001&mid=sec&listType=paper&date=20200525&page=1"
FirstPage = 1

#한 페이지당 마지막 페이지를 불러옴
def get_last_page():
    result = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
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

def extract_all_article(FirstPage, last_page):
    articles = []
    for page in range(FirstPage,last_page+1):
        result = requests.get(
            f"https://news.naver.com/main/list.nhn?mode=LSD&sid1=001&mid=sec&listType=paper&date=20200525&page={page}",
            headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div")
        print(results)

extract_all_article(1,1)