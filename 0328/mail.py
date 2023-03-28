import smtplib
from email.header import Header
from email.mime.text import MIMEText

smtp = smtplib.SMTP('smtp.naver.com', 587)
smtp.ehlo()
smtp.starttls()

smtp.login('myid','mypasswd')

myemail = 'myemail@mail.com'
youremail = 'myemail@mail.com'

subject = '파이썬을 이용한 메일 보내기'
message = '파이썬을 이용한 메일 보내기'
msg = MIMEText(message.encode('utf-8'), _subtype='plain', _charset='utf-8')
msg['Subject'] = Header(subject.encode('utf-8'), 'utf-8')
msg['From'] = myemail
msg['To'] = youremail
smtp.sendmail(myemail,youremail,msg.as_string())
smtp.quit()