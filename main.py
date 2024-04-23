import json
import requests

# 读取配置文件
with open('config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

# 从配置文件中获取accessToken和其他参数
headers = {
    "accessToken": config["accessToken"],
    "vid": config["vid"],
    "appver": config["appver"],
    "User-Agent": "WeRead/8.0.1 WRBrand/xiaomi Dalvik/2.1.0 (Linux; U; Android 13; M2007J1SC Build/TKQ1.221114.001)",
    "osver": config["osver"],
    "channelId": config["channelId"],
    "basever": config["basever"],
    "Content-Type": "application/json; charset=UTF-8",
    "Host": "i.weread.qq.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

# 目标URL
url = "https://i.weread.qq.com/ai/readbook"

# POST请求的数据
data = {
    "bookId": config["bookId"],
    "chapterUids": list(range(1, 101)),  # 生成1到100的列表
    "reqType": "keyPoint"
}

# 发送POST请求
response = requests.post(url, headers=headers, json=data)

# 检查请求是否成功
if response.status_code == 200:
    # 解析返回的JSON数据
    result = response.json()

    # 将结果保存到JSON文件中
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print("数据已成功保存到result.json文件中。")
else:
    print("请求失败，状态码：", response.status_code)
