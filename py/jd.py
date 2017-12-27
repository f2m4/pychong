import requests

def jd():
    url='https://item.jd.com/adf.aa'
    try:
        r=requests.get(url)
        r.raise_for_status()
        print(r.status_code)
        print(r.encoding)
        print(r.apparent_encoding)
        print(r.request.headers)
        print(r.headers)
        print(r.raise_for_status())

        print(r.text[:500])
    except:
        print("请求出现错误!!!")
#jd会把所有找不到的网页引导至主页
jd()
