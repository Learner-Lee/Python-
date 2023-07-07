# encoding = utf-8
# 开发者：xxx
# 开发时间： 14:06 
# "Stay hungry，stay foolish."


import requests
import json
if __name__ == '__main__':
    # 1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # 2.进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
        'Referer': 'https://fanyi.baidu.com/'
    }
    # 3.post请求参数处理（同get请求一致）
    data = {
        'kw' : 'dog'
    }
    # 4.请求发送
    response = requests.post(url=post_url, data=data, headers = headers)
    # 5.获取响应数据：json()方法返回的是obj(必须要确认是json()类型才能使用json()方法)
    dic_obj = response.json()

    # 持久化存储
    with open('./dog.json','w',encoding='utf-8') as fp:
        json.dump(dic_obj,fp=fp,ensure_ascii=False)

    print('over！！！')