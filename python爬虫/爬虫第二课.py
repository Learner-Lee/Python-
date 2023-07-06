# encoding = utf-8
# 开发者：xxx
# 开发时间： 14:49 
# "Stay hungry，stay foolish."


from urllib import request

url = 'https://hitomi.la/doujinshi/oshikko-sensei-5-%E4%B8%AD%E6%96%87-159189-914332.html#1'
# https://hitomi.la/doujinshi/oshikko-sensei-3-%E4%B8%AD%E6%96%87-158532-911990.html#1

response = request.urlopen(url) # 用于打开一个URL（包括http、https、ftp等）并获取响应。

print(response)

# 读取响应体

# print(response.read())

# 编码 文本——byte  encode
# 解码 byte——文本  decode

text = response.read().decode('utf-8')
# print(text)

with open('manhua.html','w',encoding='utf-8') as f:
    f.write(text)

# 读取响应体内容
# print(response.read().decode('utf-8'))

print(response.getcode())

print(response.geturl())

print(response.getheaders())