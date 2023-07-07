# encoding = utf-8
# 开发者：xxx
# 开发时间： 21:48 
# "Stay hungry，stay foolish."

import requests

# UA:User_Agent (请求载体的身份标识)
# UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果是浏览器则正常访问，但如果无法识别则认为是爬虫拒绝访问

# UA伪装:让爬虫对应的请求载体身份标识伪装成某一款浏览器

if __name__ == '__main__':
    url = 'https://www.sogou.com/web'
    # https://www.sogou.com/web?query=pixiv

    # UA伪装：将对应的User-Agent分装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
        'Referer': 'https://www.sogou.com/'
    }
    # 这是为了模拟浏览器发送请求时的 Referer 报头，告诉服务器我们是从 Pixiv 网站上的页面跳转过来的。
    """
    User-Agent 本机身份信息
    Referer 从哪里跳转
    """

    # 处理url携带的参数: 封装到字典中
    kw = input("enter a word:")
    param = {
        'query': kw
    }
    # 对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)

    page_text = response.text
    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, '保存成功！！！')
