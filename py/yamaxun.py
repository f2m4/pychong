import requests
def ymx(url):
    try:
        headers={
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
        }
        r=requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding="utf8"
        print(r.text)
        print(r.status_code)
    except:
        print("请求出现错误!!")
if __name__=="__main__":
    url="https://www.amazon.cn/dp/B00QJDOLIO/ref=sr_1_2?ie=UTF8&qid=1514099022&sr=8-2&keywords=kindle"
    ymx(url)