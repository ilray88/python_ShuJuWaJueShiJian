import matplotlib.pyplot as plt #导入做图库
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
x = np.random.randn(10000) #10000个服从正态分布的随机数
plt.hist(x,8) #分成8组绘制直方图
plt.show()