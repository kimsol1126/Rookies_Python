import pyperclip
import re

text = str(pyperclip.paste())
emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
jumins = re.findall(r'(\d{6})[-]\d{7}', text)

email_results = list(set(emails))
jumin_results = list(set(jumins))
print(email_results)
print(jumin_results)