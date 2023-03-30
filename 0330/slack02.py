import feedparser
import pandas as pd
from datetime import datetime
import requests
import json
import time

def news_crolling():
    url = "https://www.dailysecu.com/rss/allArticle.xml"

    feed = feedparser.parse(url)

    titles = []
    links = []
    descriptions = []
    authors = []
    pubDates = []

    for entry in feed.entries:
        titles.append(entry.title)
        links.append(entry.link)
        descriptions.append(entry.description)
        authors.append(entry.author)
        pubDates.append(entry.published)

    to_excel(titles, links, descriptions, authors, pubDates)

def to_excel(titles, links, descriptions, authors, pubDates):

    now = datetime.now().strftime("%d-%m-%Y")
    data = {'Title': titles, 'Link': links, 'Description': descriptions, 'Author': authors, 'Published': pubDates}
    df = pd.DataFrame(data)

    df.to_excel(f'dailysecu_{now}.xlsx', index=False)


def sendSlacWebhook(strText):
    slack_url = "https://hooks.slack.com/services/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"

    headers = {"Content-type": "application/json"}
    data = {"text":strText}

    response = requests.post(slack_url, headers = headers, data = json.dumps(data))
    if response.status_code == 200:
        return "잘 보냈습니다."
    else:
        return "오류 발생"
   
    
if __name__ == '__main__':
    news_crolling()
    time.sleep(5)
    print(sendSlacWebhook("뉴스 크롤링을 완료했습니다."))



