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

        f.write(f"===== 이유는 아래와 같습니다 =====\n")
        if is_malicious_ip:
            f.write(f"{ip}는 악성코드 IP로 사용되었습니다.\n")
        if opened_unusual_port:
            f.write(f"{ip}는 불필요한 포트를 사용중입니다.\n")

        f.write(f"===== {ip} 점검 완료 ===== \n\n\n")