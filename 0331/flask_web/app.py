from flask import Flask, render_template, request
import feedparser

app = Flask(__name__)

@app.route('/')
def index():
    #지정한 페이지를 렌더링. 
    #반드시 html 페이지가 templates 폴더에 있어야 함!!
    return render_template("index.html")     

@app.route('/rss', methods=['GET','POST'])
def rss():
    rss_url = request.form['rss_url'] #rss_url 이라는 이름의 값 요청
    feed = feedparser.parse(rss_url)
    return render_template("rss.html", feed=feed)

if __name__ == '__main__':
    app.run(debug=True)