# encoding = utf-8
# 开发者：xxx
# 开发时间： 14:40 
# "Stay hungry，stay foolish."


# # 下载正常图片
# import requests
#
# response = requests.get(url="https://tse2-mm.cn.bing.net/th/id/OIP-C.b39hvvD0k83rsxpCvwWf7QHaQC?w=161&h=349&c=7&r=0&o=5&dpr=2&pid=1.7")
#
# with open('107116988.png','wb') as fp:
#     fp.write(response.content)


# # 下载正常图片方法二
# import requests
#
# url = "https://tse2-mm.cn.bing.net/th/id/OIP-C.b39hvvD0k83rsxpCvwWf7QHaQC?w=161&h=349&c=7&r=0&o=5&dpr=2&pid=1.7"
#
# response = requests.get(url, stream=True)
#
# with open('107116988.jpg', 'wb') as fp:
#     for chunk in response.iter_content(chunk_size=1024):
#         if chunk:
#             fp.write(chunk)



# # 下载pixiv图片
import requests
import urllib3
# requests 是一个非常流行的 Python 库，用于发送 HTTP 请求和处理响应。
# urllib3 是一个用于发送 HTTP 请求的低级库。

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# 使用 urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 禁用了对不安全请求的警告。
# 这是因为在默认情况下，requests 库会验证 SSL 证书以确保请求的安全性。
# 但是，当我们访问 Pixiv 网站时，会遇到由于证书问题导致的警告，因此通过禁用这个警告来忽略证书验证。

headers = {'Referer': 'https://www.pixiv.net/'}
# 定义了一个 headers 字典，将 Referer 设置为 'https://www.pixiv.net/'。
# 这是为了模拟浏览器发送请求时的 Referer 报头，告诉服务器我们是从 Pixiv 网站上的页面跳转过来的。

url = 'https://i.pximg.net/c/360x360_70/custom-thumb/img/2022/06/25/14/22/59/99288135_p0_custom1200.jpg' # 目标的url
url = url.replace('c/360x360_70/custom-thumb', 'img-master')
url = url.replace('_custom', '_master')
url = url.replace('c/360x360_70/img-master', 'img-master')
url = url.replace('_square', '_master')
print(url)

res = requests.get(url, headers=headers, verify=False)  # 得到响应对象
# 使用 requests.get(url, headers=headers, verify=False) 发送了一个 GET 请求来获取图片的内容。
# headers 参数用于传递请求头信息
# verify=False 参数用于禁用对 SSL 证书的验证。

with open('test.jpg', 'wb') as f:
    f.write(res.content)
#   通过访问 res.content，我们可以获取服务器返回的响应内容，即以字节形式表示的图片数据。


# # https://i.pximg.net/c/360x360_70/custom-thumb/img/2023/06/27/20/45/38/109397070_p0_custom1200.jpg
# # https://i.pximg.net/img-master/img/2023/06/27/20/45/38/109397070_p0_master1200.jpg
# # https://i.pximg.net/c/360x360_70/custom-thumb/img/2023/06/27/22/23/56/109400234_p0_custom1200.jpg
# # https://i.pximg.net/img-master/img/2023/06/27/22/23/56/109400234_p0_master1200.jpg
# # https://i.pximg.net/c/360x360_70/img-master/img/2023/06/17/02/46/18/109076198_p0_square1200.jpg
# # https://i.pximg.net/img-master/img/2023/06/17/02/46/18/109076198_p0_master1200.jpg