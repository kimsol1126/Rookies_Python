from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("upload.html")

@app.route('/upload', methods=["POST"])
def upload():
    file = request.files["file"]
    file.save(os.path.join("uploads", file.filename))
    
    file_type = file.content_type

    # 파일 생성 시간과 접근 시간을 확인
    file_ctime = datetime.fromtimestamp(os.path.getctime(os.path.join("uploads", file.filename)))
    file_atime = datetime.fromtimestamp(os.path.getatime(os.path.join("uploads", file.filename)))

    return render_template("result.html", file_name=file.filename, file_type=file_type,
                           file_ctime=file_ctime, file_atime=file_atime)

if __name__ == '__main__':
    app.run(debug=True)