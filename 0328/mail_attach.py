import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication 

smtp = smtplib.SMTP('smtp.naver.com', 587)
smtp.ehlo()
smtp.starttls()


smtp.login('myid','mypw')

myemail = 'myemail@email.com'
youremail = 'youremail@email.com'

msg = MIMEMultipart()

msg['Subject'] ="첨부파일 테스트 입니다."
msg['From'] = myemail
msg['To'] = youremail

text = """
첨부파일 메일 테스트 내용 입니다.
감사합니다.
"""
contentPart = MIMEText(text) 
msg.attach(contentPart) 

etc_file_path = r'file_monitor.py'
with open(etc_file_path, 'rb') as f : 
    etc_part = MIMEApplication( f.read() )
    etc_part.add_header('Content-Disposition','attachment', filename=etc_file_path)
    msg.attach(etc_part)

smtp.sendmail( myemail,youremail,msg.as_string() )
smtp.quit()