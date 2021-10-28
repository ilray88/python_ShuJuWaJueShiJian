# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pyecharts

#用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
#用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

"""1、数据加载"""
#定义加载数据的文件名
#filename = "data_file\\ershoufang-mini-utf8.csv"
filename = "../data_file/new_new_utf_8.csv"
#自定义数据的行列索引（行索引使用pd默认的，列索引使用自定义的）
names = [
        "id","communityName","areaName","total","unitPriceValue",
        "fwhx","szlc","hxjg","jzmj",
        "jzlx","fwcx","jzjg","zxqk","thbl",
        "pbdt","cqnx","gpsj","jyqs","scjysj",
        "fwyt","fwnx","cqss",
        ]
#自定义需要处理的缺失值标记列表
miss_value = ["null","暂无数据"]
#数据类型会自动转换
#使用自定义的列名，跳过文件中的头行，处理缺失值列表标记的缺失值
df = pd.read_csv(filename,skiprows=[0],names=names,na_values=miss_value)
print(df.info())

"""2、数据运算"""
"""3、数据可视化呈现"""






#重庆主城区各区域二手房单价箱线图
#数据分组、数据运算和聚合
box_unitprice_area = df["unitPriceValue"].groupby(df["areaName"])
flag = True
box_data = pd.DataFrame(list(range(21000)),columns=["start"])
for name,group in box_unitprice_area:
    box_data[name] = group
del box_data["start"]

fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)
ax.set_ylabel("单价 (元/平方米)",fontsize=14)
ax.set_xlabel("区域名称",fontsize=14)
#ax.set_title("重庆主城区各区域二手房单价箱线图",fontsize=18)
box_data.plot(kind="box",fontsize=12,sym='r+',grid=True,ax=ax,yticks=[10000,20000,30000,40000,50000])


"""重庆主城区各区域二手房总价箱线图"""
#数据分组、数据运算和聚合
box_total_area = df["total"].groupby(df["areaName"])
flag = True
box_data = pd.DataFrame(list(range(21000)),columns=["start"])
for name,group in box_total_area:
    box_data[name] = group
del box_data["start"]
#mean_unitprice.index.name = ""

fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)
ax.set_ylabel("总价/万元",fontsize=14)
ax.set_xlabel("区域名称",fontsize=14)
#ax.set_title("重庆主城区各区域二手房总价箱线图",fontsize=18)
box_data.plot(kind="box",fontsize=12,sym='r+',grid=True,ax=ax,yticks=[0,100,200,300,500,1000],ylim=[0,2100])


"""重庆主城区各区域二手房平均建筑面积"""
#数据运算
#print(df["jzmj"])
groups_area_jzmj = df["jzmj"].groupby(df["areaName"])
#print(groups_area_jzmj.mean())
mean_jzmj = groups_area_jzmj.mean()
mean_jzmj.index.name = ""

#数据可视化
fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)
ax.set_ylabel("建筑面积(㎡)",fontsize=14)
ax.set_xlabel("区域名称",fontsize=14)
#ax.set_title("重庆主城区各区域二手房平均建筑面积",fontsize=18)
mean_jzmj.plot(kind="bar",fontsize=12)


"""重庆主城区各区域平均单价和平均建筑面积"""
groups_unitprice_area = df["unitPriceValue"].groupby(df["areaName"])
mean_unitprice = groups_unitprice_area.mean()
mean_unitprice.index.name = ""

groups_area_jzmj = df["jzmj"].groupby(df["areaName"])
mean_jzmj = groups_area_jzmj.mean()
print(mean_jzmj)
mean_jzmj.index.name = ""

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax1.set_ylabel("单价(元/平米)",fontsize=14)
ax.set_xlabel("区域名称",fontsize=14)
ax1.set_title("重庆主城区各区域二手房平均单价",fontsize=18)
ax2 = fig.add_subplot(2,1,2)
ax2.set_ylabel("建筑面积(㎡)",fontsize=14)
#ax2.set_title("重庆主城区各区域二手房平均建筑面积",fontsize=18)
plt.subplots_adjust(hspace=0.4)

mean_unitprice.plot(kind="bar",ax=ax1,fontsize=12)
mean_jzmj.plot(kind="bar",ax=ax2,fontsize=12)


"""重庆主城区各区域二手房房源数量"""
groups_area = df["id"].groupby(df["areaName"])
count_area = groups_area.count()
count_area.index.name = ""

fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)
ax.set_ylabel("房源数量(套)",fontsize=14)
ax.set_xlabel("区域名称",fontsize=14)
#ax.set_title("重庆主城区各区域二手房房源数量",fontsize=18)
count_area.sort_values().plot(kind="line",fontsize=12,grid=True,marker="o")


"""重庆主城区二手房单价最高Top20"""
unitprice_top = df.sort_values(by="unitPriceValue",ascending=False)[:20]
unitprice_top = unitprice_top.sort_values(by="unitPriceValue")
unitprice_top.set_index(unitprice_top["communityName"],inplace=True)
unitprice_top.index.name = ""

fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)
ax.set_xlabel("单价(元/平方米)",fontsize=14)
#ax.set_title("重庆主城区二手房单价最高Top20",fontsize=18)
unitprice_top["unitPriceValue"].plot(kind="barh",fontsize=12)


"""重庆主城区二手房总价与建筑面积散点图"""
fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)
#ax.set_title("重庆主城区二手房总价与建筑面积散点图",fontsize=18)
df.plot(x="jzmj", y="total", kind="scatter",fontsize=12,ax=ax,alpha=0.4,xticks=[0,50,100,150,200,250,300,400,500,600,700],xlim=[0,800])
ax.set_xlabel("建筑面积/㎡",fontsize=14)
ax.set_ylabel("总价/万元",fontsize=14)

"""重庆主城区二手房单价与建筑面积散点图"""
fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)
#ax.set_title("重庆主城区二手房单价与建筑面积散点图",fontsize=18)
df.plot(x="jzmj",y="unitPriceValue",kind="scatter",grid=True,fontsize=12,ax=ax,alpha=0.4,xticks=[0,50,100,150,200,250,300,400,500,600,700],xlim=[0,800])
ax.set_xlabel("建筑面积/㎡)",fontsize=14)
ax.set_ylabel("单价 (元/平方米)",fontsize=14)
plt.show()
