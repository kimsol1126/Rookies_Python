from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime
import requests
import json

api_key = "your API Key"
base_url = "https://api.criminalip.io/v1/feature/ip/is_safe_dns_server"
current_date = datetime.now().strftime("%Y-%m-%d")

ip = input(f"확인할 IP 주소를 입력하세요. ")
url = f"{base_url}?ip={ip}"
output_path = f"result_{current_date}.txt"

headers = {"x-api-key": api_key}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    is_safe_dns_server = data["is_safe_dns_server"]
    is_malicious_ip = data["reason"]["is_malicious_ip"]
    opened_unusual_port = data["reason"]["opened_unusual_port"]
    is_unpublic_dns = data["reason"]["is_unpublic_dns"]

    with open(output_path, "a", encoding="utf-8") as f:
        if is_safe_dns_server:
            f.write(f"{ip}는 안전한 DNS 서버입니다.\n")
            print(f"{ip}는 안전한 DNS 서버입니다.")
        else:
            f.write(f"{ip}는 안전한 DNS 서버가 아닙니다.\n")
            print(f"{ip}는 안전한 DNS 서버가 아닙니다.")

# Slack channel to send the message to
SLACK_API_TOKEN = "xoxb-5018816800775-5057123056800-AtAn6c5Y3mjBCURdrfGBUx2c"


def sendSlackWebhook(file_path):
    client = WebClient(token=SLACK_API_TOKEN)
    try:
        response = client.files_upload(
            channels="#파이썬-교육",
            file=file_path,
            #title=f"Result of DNS server safety check ({current_date})"
            title = f"{current_date}의 파일 전송이 완료되었습니다.."
        )
        print(f"Uploaded the file {file_path} to Slack")
    except SlackApiError as e:
        print(f"Error uploading the file: {e}")


sendSlackWebhook(output_path)