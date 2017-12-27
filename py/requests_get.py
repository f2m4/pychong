import requests

r=requests.get("http://www.baidu.com")
print(r.status_code)
print(r.encoding)
print(r.apparent_encoding)
r.encoding=r.apparent_encoding
print(r.text)