import matplotlib.pyplot as plt #导入做图库
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
x = np.linspace(0,2*np.pi,50) #x坐标输入
y = np.cos(x)
plt.plot(x,y,'g--')
plt.show()