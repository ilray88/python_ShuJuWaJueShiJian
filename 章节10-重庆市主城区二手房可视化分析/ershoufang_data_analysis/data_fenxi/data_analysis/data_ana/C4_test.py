# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 数据读取
data = pd.read_csv('../data_file/new_new_utf_8.csv',encoding='utf-8')
print(data.head())#查看数据

def d_range(df,*cols):
    krange = []
    for col in cols:
        crange = df[col].max() - df[col].min()
        krange.append(crange)
    return(krange)
# 创建函数求极差

key1 = '单价'
key2 = '总价'
dr = d_range(data,key1,key2)
print('%s极差为 %f \n%s极差为 %f' % (key1, dr[0], key2, dr[1]))

print(data[key2].hist(bins=10))