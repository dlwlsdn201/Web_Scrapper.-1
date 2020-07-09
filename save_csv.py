import csv
from _datetime import datetime
def save_to_csv(articles):
    date = datetime.today().strftime("%Y%m%d%H%M%S")
    date = date[:8]
    hour = datetime.today().hour
    minute = datetime.today().minute
    file = open(f"./csvData/naver_IT_articles__{date}_{hour}시_{minute}분.csv", mode="w", encoding="UTF-8", newline='')
    writer = csv.writer(file)
    writer.writerow(["제목", "신문사", "바로가기"])
    for article in articles:
        writer.writerow(list(article.values()))
    return