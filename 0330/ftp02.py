import ftplib
import zipfile
import os
from datetime import datetime

now = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

def zipper():
    directory = "static" #static 이라는 폴더 사용
    #비어있는 압축파일 하나 생성
    zip_file = zipfile.ZipFile(f'{now}.zip', 'w')
    for root, dirs, files in os.walk(directory):
        for file in files:
            zip_file.write(os.path.join(root, file)) #경로지정
    #안에 폴더가 있어도 알아서 다 압축해줌
    zip_file.close()    

def ftp_upload():
    ftp_host = "192.168.153.128"
    ftp_user = "kali"
    ftp_pass = "kali"

    ftp = ftplib.FTP(ftp_host)
    ftp.login(ftp_user, ftp_pass)

    print(f"현재 작업 디렉터리: {ftp.cwd('ftp')}") #디렉터리 변경 
    with open(f"{now}.zip", "rb") as f:
        #ftp는 파일을 바이너리 형태로 전송
        ftp.storbinary(f"STOR {now}.zip", f)

    #보낸 후 진짜 업로드되었는 지 확인
    print(f"현재 작업 디렉터리: {ftp.pwd()}")
    print(ftp.dir())

    ftp.quit()

zipper()
ftp_upload()