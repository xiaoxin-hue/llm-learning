# 标准库导入
import math
import datetime as dt  # 可以起别名

# 第三方库导入（需要先 pip install requests）
import requests

# 使用标准库
print(math.sqrt(16))                    # 4.0
print(dt.datetime.now())                # 当前时间

# 使用第三方库（示例：发送 GET 请求获取网页状态）
response = requests.get("https://www.baidu.com")
print(f"状态码: {response.status_code}") # 200
