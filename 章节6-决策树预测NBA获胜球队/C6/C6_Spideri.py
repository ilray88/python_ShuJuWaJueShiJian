from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
BASE_URL = 'https://www.basketball-reference.com/leagues/NBA_2016_games-{month}.html'
all_month = np.array(['october','november','december','january','february','march','april','may','june'])
def get_content():
    list = []
    for i in range(len(all_month)):
        url = BASE_URL.format(month=all_month[i])
        print(url)
        html = urlopen(url).read()
        bsObj = BeautifulSoup(html,'lxml')
        rows = [dd for dd in bsObj.select('tbody tr')]
#selectk()可以多重刷选
    for row in rows:
     cell = [i.text for i in row.find_all('td')]
#对于每一个tr标签内也可以进行td标签筛选
    list.append(cell)
    return list#返回二维列表
def save():
    file = open('E:/python/PycharmProjects/untitled/C6/matches.csv','w')
    list = get_content()
    df_data = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9] ,data=list)
    df_data.to_csv(file)
    print('done')
if __name__ == "__main__":
    print(save())
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import re
pattern = re.compile('<tbody>[\s\S]*?</tbody>')#模仿html注释的正则
url = 'https://www.basketball-reference.com/leagues/NBA_2015_standings.html'
html = urlopen(url).read()
bsObj = BeautifulSoup(html,'lxml')
content = bsObj.find(id='all_expanded_standings').prettify()
match = re.search(pattern,content)
str_tbody = match.group()
html_tbody = BeautifulSoup(str_tbody,'lxml')#将str字符串传入获得html对象
list = []
for tr in html_tbody.find_all('tr'):
    rows = [td.text for td in tr.find_all('td')]
    list.append(rows)
#转成csv格式
file = 'E:/python/PycharmProjects/untitled/C6/new_standing.csv'#自行修改
df_data = pd.DataFrame(data=list)
df_data.to_csv(file)