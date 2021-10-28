import matplotlib.pyplot as plt #导入做图库
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
labels = ['pineapple ','watermelon',' shaddock','lemon'] #每一块标签
sizes = [20,20,45,15] #每一块比例
colors = ['yellowgreen','gold','lightskyblue','lightcoral'] #每一块颜色
explode = (0,0,0.1,0) #突出显示第二块
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')
plt.show()