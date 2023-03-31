from datetime import datetime
import requests
import json

api_key = "Your API Key"
base_url = "https://api.criminalip.io/v1/feature/ip/is_safe_dns_server"

ip = input(f"확인할 IP 주소를 입력하세요. ")
url = f"{base_url}?ip={ip}"

headers = {"x-api-key": api_key}

response = requests.get(url, headers=headers)
print(response.text)
print(response.json())