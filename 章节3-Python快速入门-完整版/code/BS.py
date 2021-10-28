import requests
from bs4 import BeautifulSoup
r=requests.get('http://www.sina.com.cn')
r.encoding = 'utf-8'
demo=r.text
print(demo)
soup=BeautifulSoup(demo,'html.parser')
print(soup.prettify()) #perttify()让HTML页面以更加“友好”的方式显示

import requests
from bs4 import BeautifulSoup
r=requests.get('http://www.sina.com.cn')
r.encoding = 'utf-8'  #设置编码格式
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
print(soup.title)  #<title>新浪首页</title>
print(soup.a)
print(soup.a.name)
print(soup.a.parent.name)
print(soup.a.attrs)
print(soup.p.string)
print(type(soup.p.string))
print(soup.b.string)