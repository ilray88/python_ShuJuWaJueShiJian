# -*- coding: utf-8 -*-


import json
from urllib.request import quote
import requests
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def getlnglat(address):
    """
    获取一个中文地址的经纬度(lat:纬度值,lng:经度值)
    """
    url_base = "http://api.map.baidu.com/geocoder/v2/"
    output = "json"
    ak = "5VlZh7U5gYagujGlrTtNFErWyWqRFLNG" # 浏览器端密钥
    address = quote(address) # 由于本文地址变量为中文，为防止乱码，先用quote进行编码
    url = url_base + '?' + 'address=' + address  + '&output=' + output + '&ak=' + ak 
    lat = 0.0
    lng = 0.0
    res = requests.get(url)
    temp = json.loads(res.text)
    if temp["status"] == 0:
        lat = temp['result']['location']['lat']
        lng = temp['result']['location']['lng']
    return lat,lng


#用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
#用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

"""1、数据加载"""
#定义加载数据的文件名
#filename = "data_file\\ershoufang-mini-utf8.csv"
filename = "../data_file/ershoufang-clean-utf8-v1.1.csv"
#自定义数据的行列索引（行索引使用pd默认的，列索引使用自定义的）
names = [
        "id","communityName","areaName","total","unitPriceValue",
        "fwhx","szlc","jzmj","hxjg","tnmj",
        "jzlx","fwcx","jzjg","zxqk","thbl",
        "pbdt","cqnx","gpsj","jyqs","scjy",
        "fwyt","fwnx","cqss","dyxx","fbbj",
        ]
#自定义需要处理的缺失值标记列表
miss_value = ["null","暂无数据"]
#数据类型会自动转换
#使用自定义的列名，跳过文件中的头行，处理缺失值列表标记的缺失值
df = pd.read_csv(filename,skiprows=[0],names=names,na_values=miss_value)


"""2、生成经纬度信息"""
idint = []
names = []
lats = []
lngs = []
lat_lng_data = {"id":idint,"communityName":names,"lat":lats,"lng":lngs}

#flag = 0
for idi,name in zip(list(df["id"]),list(df["communityName"])):
    name = str(name)
    lat,lng = getlnglat("南京市"+name)
    if lat != 0 or lng !=0:
        idint.append(idi)
        names.append(name)
        lats.append(lat)
        lngs.append(lng)
        print(idi)
    
frame_test = pd.DataFrame(lat_lng_data)
frame_test.to_csv("../data_file/latlng.csv")


"""3、合并数据，并按格式输出数据"""
#合并数据
df_latlng = pd.read_csv("../data_file/latlng.csv",skiprows=[0],names=["did","communityName","id","lat","lng"])
del df_latlng["did"]
del df_latlng["communityName"]

df_merge = pd.merge(df,df_latlng,on="id")

#小于200万
xiaoyu = df_merge[df_merge["total"]<201]
xiaoyu2 = df_merge.loc[df_merge["total"]<201]
xiaoyu2 = xiaoyu2.loc[xiaoyu2["jzmj"] < 50]


"""4、生成需要的格式文件"""
out_map = "../data_file/star.txt"
with open(out_map,"w") as file_out:
    for lng,lat,price in zip(list(xiaoyu["lng"]),list(xiaoyu["lat"]),list(xiaoyu["total"])):
        out = str(lng)+","+str(lat)
        #out='{\"lng\":'+str(lng)+',\"lat\":'+str(lat)+',\"count\":'+str(price)+'},'
        file_out.write(out)
        file_out.write("\n")

file = open(r'cluster0.js','w') #建立json数据文件
with open(r'E:\\爬虫数据分析\调用百度地图api\各区域房价.csv', 'r') as csvfile: #打开csv
    reader = csv.reader(csvfile)
    for line in reader: #读取csv里的数据
        # 忽略第一行
        if reader.line_num == 1: #由于第一行为变量名称，故忽略掉
            continue
            # line是个list，取得所有需要的值
        b = line[0].strip() #将第一列city读取出来并清除不需要字符
        c= line[1].strip()#将第二列price读取出来并清除不需要字符
        lng = getlnglat(b)['result']['location']['lng'] #采用构造的函数来获取经度
        lat = getlnglat(b)['result']['location']['lat'] #获取纬度
        str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(c) +'},'
        #print(str_temp) #也可以通过打印出来，把数据copy到百度热力地图api的相应位置上
        file.write(str_temp) #写入文档
file.close() #保存