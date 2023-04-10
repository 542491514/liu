import requests
import json

response = requests.get('http://127.0.0.1:5000/hello')
# 使用request请求一个json
response = response.text
print(response)
# 使用requests的的text方法取出响应的文本
dict = json.loads(response)
# 使用JSON模块的loads方法，可以将这个字符串转化为字典
print(dict)
#打印这个字典
print(type(dict))
#确认是否为字典类型

#以下是字典操作方法，将字典的数据取出并打印
print('响应状态：'+dict.get('status'))
print('返回信息：'+dict.get('message'))
print('编号：'+dict.get('no'))
print('网站名称：'+dict.get('name'))
print('网站url：'+dict.get('url'))


response = requests.get('http://127.0.0.1:5000/hello2')
# 使用request请求一个json
response = response.text
# 使用requests的的text方法取出响应的文本
dict = json.loads(response)
# 使用JSON模块的loads方法，可以将这个字符串转化为字典
print(dict)
#打印这个字典
print(type(dict))
#确认是否为字典类型

#以下是字典操作方法，将字典的数据取出并打印
print('响应状态：'+dict.get('status'))
print('返回信息：'+dict.get('message'))
print('编号：'+dict.get('no'))
print('网站名称：'+dict.get('name'))
print('网站url：'+dict.get('url'))