
# 网络机器人-合规性 (robots协议)

**1. 什么是robots协议？**
*   又称：**爬虫协议、爬虫规则**。
*   **位置**：网站根目录下存放的一份文本文件 `robots.txt`。
*   **作用**：用于告诉爬虫哪些页面**可以**抓取，哪些页面**不能**抓取。
*   **别称**：君子协议（依赖爬虫开发者自觉遵守）。

**2. robots.txt 语法及字段说明**

*   **`User-Agent`**：用户代理。通过该请求头确认爬虫的类型（如：通用爬虫、特定网站爬虫）。
*   **`Disallow`**：禁止访问的资源路径。
*   **`Allow`**：允许访问的资源路径。
*   **`Sitemap`**：网站地图。帮助爬虫更高效地获取网站内容。
*   **`Crawl-delay`**：爬取间隔时间。避免频繁访问造成网站压力过大。

**3. `robots.txt` 代码示例解析**

三种不同的规则配置情况：

*   **情况一：通用规则（针对所有爬虫）**
    ```text
    User-agent: *              # * 代表针对所有爬虫
    Disallow: /wp-admin/       # 禁止访问 wp-admin 目录
    Allow: /wp-admin/admin-ajax.php # 允许访问该特定 php 文件 (特例)
    Sitemap: https://www.tiobe.com/sitemap_index.xml # 指定网站地图地址
    Crawl-delay: 5             # 每次爬取间隔 5 秒
    ```

*   **情况二：特定规则（针对豌豆荚爬虫）**
    ```text
    User-agent: Wandoujia Spider # 针对豌豆荚的爬虫
    Disallow: /                  # 禁止访问该网站的所有内容
    ```

*   **情况三：特定规则（针对谷歌广告爬虫）**
    ```text
    User-agent: Mediapartners-Google # 针对谷歌广告爬虫
    Disallow: /subject_search    # 禁止访问特定搜索目录
    Disallow: /amazon_search
    Disallow: /search
    Disallow: /group/search
    ```