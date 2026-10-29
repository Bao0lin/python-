# 下载requests库

pip install requests

# 发送请求

```python
import requests
# 定义url
target_url = "https://merchant.fleetingpower.com/login"
#发送请求，获取数据
response = requests.get(target_url)
# 输出数据到控制台
print(response.text)     # 获取网页的源代码（字符串格式，最常用）
print(response.content)  # 获取网页的二进制数据（下载图片、视频时用）
print(response.status_code) # 只获取状态码数字 200
print(response.headers)  # 获取响应头（里面可能有反爬信息）
print(response.json())   # 如果请求的是 API 接口返回的是 JSON 数据，用这个直接转成字典

# 如果只写
print(response)  #显示<Response [200]>
```

# 网页状态码
HTTP 状态码（HTTP Status Code）。它就像是服务器给你的“回执单”上的盖章。常见的状态码有：

200 OK：请求成功（最常见）。
301 / 302：重定向（网页搬家了）。
403 Forbidden：禁止访问（可能被反爬虫拦截了，或者没有权限）。
404 Not Found：找不到页面（链接写错了，或者页面被删除了）。
500 Internal Server Error：服务器内部错误（服务器自己崩了）


# 前端网页结构

**核心概念：**
一个完整的网页通常由三个部分组成，分别是：**HTML、CSS、JS (JavaScript)**。

**三大部分的具体职责：**
*   **HTML（超文本标记语言）—— 负责“结构”**
    *   由一堆预设的标签构成（例如：`<h1>一级标题</h1>`）。
    *   负责网页的结构（即页面元素和具体内容）。

*   **CSS（层叠样式表）—— 负责“表现”**
    *   负责网页元素的外观和位置等样式。
    *   例如：控制颜色、大小、排版布局等。

*   **JS（全称 JavaScript）—— 负责“行为”**
    *   负责网页的交互效果。
    *   让网页“动”起来，响应用户的操作。

