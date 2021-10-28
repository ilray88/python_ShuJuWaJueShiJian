import pandas as pd
from scipy.interpolate import lagrange
data=pd.read_excel(r'catering_sale.xls')
# 过滤异常值，将其变为空值
data['销量'][(data['销量']<400)|(data['销量']>5000)]=None
#自定义列向量插值函数
def ployinterp_column(s,n,k=5):
    y=s[list(range(n-k,n))+list(range(n+1,n+1+k))]  #取数
    y=y[y.notnull()]    #剔除空值
    return lagrange(y.index,list(y))(n)  #插值并返回插值结果
#逐个元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]: #如果为空即插值
            data[i][j]=ployinterp_column(data[i],j)