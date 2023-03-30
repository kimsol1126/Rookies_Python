import ftplib

ftp_host = "192.168.153.128"
ftp_user = "kali"
ftp_pass = "kali"

ftp = ftplib.FTP(ftp_host)
ftp.login(ftp_user, ftp_pass)

print(f"현재 작업 디렉터리: {ftp.cwd('ftp')}") #디렉터리 변경 
with open("ftp_test.txt", "rb") as f:
    #ftp는 파일을 바이너리 현태로 전송
    ftp.storbinary(f"STOR ftp_test.txt", f)

#보낸 후 진짜 업로드되었는 지 확인
print(f"현재 작업 디렉터리: {ftp.pwd()}")
print(ftp.dir())

ftp.quit()