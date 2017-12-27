import re,requests,bs4,lxml
from bs4 import BeautifulSoup
def getHtml(url):
    headers={
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
    }
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''
def saveList(ulist,html):
    soup=BeautifulSoup(html,"lxml")
    tbodylist=soup.find("tbody")("tr")
    for i in tbodylist:

def printList(ulist):
    pass
if __name__ == '__main__':
    url='http://www.gaokaopai.com/paihang-otype-2.html?f=1&ly=bd&city=&cate=&batch_type='
    ulist=[]
    html=getHtml(url)
    saveList(ulist,html)
    printList(ulist)