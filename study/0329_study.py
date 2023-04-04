import feedparser
import pandas as pd
from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime
import json
import requests
import schedule
import time

url = "http://www.boannews.com/media/news_rss.xml?mkind=1"
SLACK_API_TOKEN = "xoxb-5018816800775-5057123056800-TQG1Wu6XETx1IV9vNySEv8v7"
slack_url = "https://hooks.slack.com/services/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"

feed = feedparser.parse(url)
now = datetime.now().strftime("%Y-%m-%d")

#print(feed.entries) #<item>태그 안의 정보들만 가져오기
def today_boan():
    titles = []
    links = []
    descriptions = []

    for entry in feed.entries:
        titles.append(entry.title)
        links.append(entry.link)
        descriptions.append(entry.description)

    data = {'Title': titles, 'Link': links, 'Description': descriptions}
    df = pd.DataFrame(data)

    df.to_excel(f'boannews_{now}.xlsx', index=False)
    main_news = titles[0]+' / '+links[0]

    return main_news

def sendSlackWebhookfile(file_path):
    client = WebClient(token=SLACK_API_TOKEN)

    try:
        response = client.files_upload(
            channels="#파이썬-교육",
            file=file_path,
            title = f"{now}의 보안뉴스입니다."
        )
        print(f"Uploaded the file {file_path} to Slack")
    except SlackApiError as e:
        print(f"Error uploading the file: {e}")

def sendSlacWebhookmsg(msg):

    headers = {"Content-type": "application/json"}
    data = {"text":msg}

    response = requests.post(slack_url, headers = headers, data = json.dumps(data))
    if response.status_code == 200:
        return "잘 보냈습니다."
    else:
        return "오류 발생"
 
def daliy_routine():
    msg = today_boan()
    output_path = f"boannews_{now}.xlsx"
    sendSlacWebhookmsg(msg)
    sendSlackWebhookfile(output_path)

if __name__ == '__main__':
    schedule.every().day.at("09:30").do(daliy_routine)

    while True:
        schedule.run_pending()
        time.sleep(1)