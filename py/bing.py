import requests,re

def bing(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
    }
    try:
        r=requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        repic=re.compile('background-image:url\((.*)\)',re.S)
        picurl="https://www.bing.com"
        print('begin')
        picurl1=repic.findall(r.text)
        # print(r.text)
        print(picurl1)
        print(len(picurl1))
    except:
        return "访问错误!!!"
if __name__=="__main__":
    url='https://www.bing.com/'
    bing(url)