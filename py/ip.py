import requests,re

def ipsearch(ip):
    url="http://ip138.com/ips138.asp"
    kv={
        'ip':ip
    }
    try:
        r=requests.get(url,params=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "访问出现错误"

if __name__=="__main__":
    reip=re.compile(r'<ul class="ul1">(.*?)</ul>',re.S)
    print("请输入需要查询的ip地址,回车确认:")
    ip=input()
    while(ip!='q'):
        print(reip.findall(ipsearch(ip)))
        print("请输入需要查询的ip地址,输入q退出,回车确认:")
        ip = input()
    
