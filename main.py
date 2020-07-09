import naver
from save_csv import save_to_csv as save


def init():
    obj1 = naver.the_latest_ITNews(1,f'https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=105&date=20200709&page=1')
    articles_list = obj1.main() #naver IT 최신뉴스 기사 추출하는 모델의 main 함수 실행.
    print(articles_list)
    save(articles_list) #csv 파일로 저장.

init()