#直方图用hist函数来绘制。直方图描述了数据中某个范围内数据出现的频度。
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
mu, sigma = 100, 20  # 均值和标准值
a = np.random.normal(mu, sigma, size=100)
plt.hist(a,20,histtype='stepfilled', facecolor='b', alpha=0.75)#教材中代码中包含属性normed，保留normed报错的原因是因为版本更新，该属性被删除，此处可将该属性删掉。
plt.title('Histogram')
plt.show()