from flask import Flask, render_template, request, jsonify, redirect
from slack_sdk.errors import SlackApiError
from bs4 import BeautifulSoup
import requests
import time
import json
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

headers={'Content-Type': 'application/json'}

SLACK_URL = '...'
keyword = ''

# 구글 뉴스 메인 URL
GOOGLE_URL = 'https://news.google.com'

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/search', methods=['GET','POST']) 
def search(): # 검색 기능
    keyword = request.form['keyword'] 
    limit = int(request.form['limit'])
    results = [] 
    url = GOOGLE_URL + '/qsearch?=' + keyword + '&hl=ko&gl=KR&ceid=KR%3Ako' 
    response = requests.get(url) 
    soup = BeautifulSoup(response.content, 'html.parser') 
    articles = soup.find_all('div', {'class': 'NiLAwe'}) 
    
    for article in articles: 
        if keyword in article.h3.a.text: 
            result = {}
            result['title'] = article.h3.a.text
            result['link'] = GOOGLE_URL + article.h3.a['href']
            results.append(result) 
            if len(results) >= limit:
                break
            time.sleep(0.5) # 차단 방지용
    for idx, result in enumerate(results):
        result['id'] = idx + 1 # 순서번호
    return render_template('search.html', keyword=keyword, results=results)
    # search.html 파일을 렌더링하여 보여줌, keyword와 results 파라미터를 전달
    
@app.route('/send', methods=['POST','GET']) 
def send_slack(): # 슬랙 전송 기능
    # 메시지 전송
    selected = request.form.getlist('selected[]') 
    keyword = request.form['keyword'] 
    select_news = []
    #메일 전송
    smtp = smtplib.SMTP('smtp.naver.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ID','pw')

    myemail = 'email@mail.com'
    youremail = request.form['email']
    
    try: 
        # id 추출, 추출한 id로 url 추출
        # 슬랙
        for s in selected:
            id = int(s) # 정수형으로 id 저장
            url = request.form['url_'+str(id)] 
            title = request.form['title_'+str(id)]
           
            data = {
                'text': '[' + str(id) + ']번 '+ keyword + ' 관련 기사  제목: '+ title + ' \n 링크 : ' + url # 슬랙에 출력될 메시지
            }
            message_response = requests.post(SLACK_URL, headers=headers, data=json.dumps(data)) # 슬랙 봇에 메시지를 전송, request 모듈을 사용해 POST 요청
            select_news.append(f'제목: {title} / 링크: {url}\n')
        
        # 메일
        print(f"data:{select_news}")
        subject = f'{keyword} 관련 구글 뉴스' 
        message = f'{keyword}(과/와) 관련된 선택한 뉴스 목록입니다. \n'
        for news in select_news:
            message = f'{message + news}\n' 
        msg = MIMEText(message.encode('utf-8'), _subtype='plain', _charset='utf-8')
        msg['Subject'] = Header(subject.encode('utf-8'), 'utf-8')
        msg['From'] = myemail
        msg['To'] = youremail
        smtp.sendmail(myemail,youremail,msg.as_string())
        smtp.quit() 
        
        return redirect('/') # 초기 화면으로 돌아감
    
    except SlackApiError as e: # try부분의 코드 동작 실패 시
        return jsonify({'error':e}) 
   
if __name__ == '__main__':
    app.run(port=8080, debug=True) # localhost:8080으로 접속