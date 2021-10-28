# -!- coding: utf-8 -!-
import requests
import re
import time
from requests.exceptions import RequestException
import csv

def get_one_page(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return 0
    except RequestException:
        return 0

def spider(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)

def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?title="(.*?)".*?img data-src="(.*?)".*?<p class="star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i><i class="fraction">(\d+).*?</dd>',re.S
    )
    items = re.findall(pattern,html)
    for item in items:
        yield{
            'index':item[0],
            'title':item[1],
            'actor':item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time':item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score':item[5].strip()+item[6].strip(),
        }

def write_to_file(content):
    with open('maoyanSpider.csv','a',newline='')as csvfile:
        writer = csv.writer(csvfile)
        values = list(content.values())
        writer.writerow(values)

if __name__=='__main__':
    for i in range(10):
        spider(offset=10*i)
        time.sleep(1)