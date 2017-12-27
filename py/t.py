import re,requests,bs4,lxml
from bs4 import BeautifulSoup

soup=BeautifulSoup(open("t.html"),'lxml')
pdom=soup.find_all("p")
print(type(pdom))
