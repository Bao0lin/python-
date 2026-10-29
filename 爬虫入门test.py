import requests
# 定义url
target_url = "https://merchant.fleetingpower.com/login"
#发送请求，获取数据
response = requests.get(target_url)
# 输出数据到控制台
print(response.text)     # 获取网页的源代码（字符串格式，最常用）