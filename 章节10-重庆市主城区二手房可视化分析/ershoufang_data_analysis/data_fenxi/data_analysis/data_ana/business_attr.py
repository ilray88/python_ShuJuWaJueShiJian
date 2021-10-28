# -*- coding: utf-8-*-
import matplotlib.pyplot as plt
import pandas as pd

#用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
#用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
"""1、数据加载"""
#定义加载数据的文件名
filename = "../data_file/new_new_utf_8.csv"
#使用相对路径
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
"""2、数据可视化呈现"""
"""重庆二手房房屋用途占水平柱状图"""
count_fwyt = df["fwyt"].value_counts(ascending=True)
count_fwyt.name = ""
fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)
ax.set_xlabel("房源数量(套)",fontsize=14)
ax.set_title("重庆二手房房屋用途水平柱状图",fontsize=18)
count_fwyt.plot(kind="barh",fontsize=12)
plt.show()