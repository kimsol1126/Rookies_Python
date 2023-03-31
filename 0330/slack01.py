#curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' https://hooks.slack.com/services/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

import requests
import json

slack_url = "https://hooks.slack.com/services/T050JQ0PJNT/B0511SCTNG4/…"

def sendSlacWebhook(strText):
    headers = {"Content-type": "application/json"}
    data = {"text":strText}

    response = requests.post(slack_url, headers = headers, data = json.dumps(data))
    if response.status_code == 200:
        return "잘 보냈습니다."
    else:
        return "오류 발생"
    

print(sendSlacWebhook("테스트입니다.!!"))
