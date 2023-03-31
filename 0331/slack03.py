from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime

# Slack channel to send the message to
SLACK_API_TOKEN = "your API Token"
current_date = datetime.now().strftime("%Y-%m-%d")

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

output_path = "slackfile_test.txt"
sendSlackWebhook(output_path)