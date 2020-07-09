#네이버 IT/과학 뉴스 속보 기사 크롤링
import csv
import requests
from bs4 import BeautifulSoup

class the_latest_ITNews: #Naver 뉴스
    def __init__(self, FirstPage, URL):
        self.news_url = f"{URL}"
        self.firstPage = FirstPage

    #한 페이지당 마지막 페이지를 불러옴
    def get_last_page(self):
        result = requests.get(self.news_url, headers={"User-Agent": "Mozilla/5.0"})
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

    def extract_all_articles(self,last_page):
        articles_list = []
        for page in range(self.firstPage,last_page+1):
            result = requests.get(
                f"{self.news_url[:-1]}{page}",
                headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(result.text, "html.parser")
            results_all = soup.find('td',{'class':'content'})
            results_half1 = results_all.find('ul',{'class':'type06_headline'}).find_all('li')
            results_half2 = results_all.find('ul',{'class':'type06'}).find_all('li')
            articles = [results_half1,results_half2]
            for results in articles:
                for result in results:
                    article = self.extract_each_article(result)
                    articles_list.append(article)  #각 기사의 title/언론사/링크 추출한 값을 뉴스기사 리스트에 추가.
        return articles_list


    def extract_each_article(self,html):
        #기사 제목 추출 조건문
        if html.find('dt',{'class':'photo'}) :
            title = html.find("img")["alt"]
        else:
            title = html.find('a',{'class':'nclicks(fls.list)'}).get_text(strip=True)
        url = html.find("a")["href"]
        press = html.find('span',{'class':'writing'}).get_text(strip=True)
        return {'제목' : title, '신문사' : press , '바로가기' : url}


    def main(self):
        last_pagination = self.get_last_page()
        get_articles = self.extract_all_articles(last_pagination)
        return get_articles
