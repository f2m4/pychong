# -*- coding=utf8 -*-
import re,time,requests,html
from bs4 import BeautifulSoup

def qiu_page(page):
    url='https://www.qiushibaike.com/text/page/'+str(page)
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Referer':'https://www.qiushibaike.com/text/'
    }
    response=requests.get(url,headers=headers)
    # print(response.status_code)
    # print(response.encoding)
    content_div=re.compile('<div class="content"><span>(.*?)</span></div>',re.S)
    body=html.unescape(response.text).replace("<br/>","")
    body=body.replace("\n","")
    m=content_div.findall(body)
    print(m)


qiu_page(1)
