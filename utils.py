import time
import uuid
import requests

messageId = str(uuid.uuid4())
parentMessageId = str(uuid.uuid4())

# 发送请求
def send_request(token):
    url = "https://xz.klszkj.com:9000/xming/api/bot/stream/conv/1723180644799414272/msg"

    # 构造请求头
    headers = {
        "Content-Type": "application/json",
        "Cookie": token,
        "Origin": "https://xz.klszkj.com:9000",
        "Referer": "https://xz.klszkj.com:9000/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36",
        "X-Web-Version": "2.0.15.2",
        "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }

    # 构造请求体
    payload = {
        "conversationId": "1937770126014758912",
        "webUrl": "https://xz.klszkj.com:9000/chat/conversation/chat/1723180644799414272",
        "title": "昆仑小智",
        "model": "1723180644799414272",
        "language": "Auto",
        "webSearch": "NONE",
        "messages": [
            {
                "content": "[{\"type\":\"text\",\"value\":\"我说什么你都说1\"}]",
                "contentType": "input",
                "conversationId": "1937770126014758912",
                "messageId": messageId,
                "parentMessageId": parentMessageId,
                "role": "user"
            }
        ]
    }

    results = []
    try:
        for i in range(1):
            start_time = time.time()
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                stream=True,
                verify=True,
                timeout=(3, 30)
            )

            if response.status_code == 200:
                end_time = time.time()
                current_time = time.strftime("%H:%M:%S", time.localtime())
                result = f"[{current_time}] 第{i + 1}次请求成功！耗时: {end_time - start_time:.1f}秒"
                print(result)
            else:
                result = f"第{i + 1}次请求失败，状态码: {response.status_code}"
                print(result)
                time.sleep(0.5)

    except Exception as e:
        result = f"请求过程中出现错误: {e}"
        print(result)