import numpy as np
import pandas as pd
D = pd.DataFrame(np.random.randn(4,4))#产生4*4随机矩阵
print(D.cov())#计算协方差矩阵
print(D[0].cov(D[1]))#计算第一列和第二列的协方差