#使用Python数组创建
import pandas as pd
import numpy as np
#Series的字符串表现形式为：索引在左边，值在右边
obj = pd.Series([4, 7, -5, 3])
print(obj.values)
print(obj.index)
#与普通numpy数组相比，可以通过索引的方式选取Series中的单个或一组值。
print(obj[2])
obj[1]=8
print(obj[[0, 1, 3]])
#Series中最重要的一个功能是：它会在算术运算中自动对齐不同索引的数据。
obj2 = pd.Series({"Ohio": 35000, "Oregon": 16000, "Texas": 71000, "Utah": 5000})
obj3 = pd.Series({"California": np.nan, "Ohio": 35000, "Oregon": 16000, "Texas": 71000})
print(obj2 + obj3)


#Series对象本身及其索引都有一个name属性，该属性跟pandas其他的关键功能关系非常密切。
obj3.name= 'population'
obj3.index.name = 'state'
print(obj3)