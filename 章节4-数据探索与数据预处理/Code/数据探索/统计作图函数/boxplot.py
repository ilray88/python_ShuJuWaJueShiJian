import matplotlib.pyplot as plt #导入做图库
import pandas as pd
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
x = np.random.randn(10000) #10000个服从正态分布的随机数
D = pd.DataFrame([x,x+1]).T
D.plot(kind='box')
plt.show()