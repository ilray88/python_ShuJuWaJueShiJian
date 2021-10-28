import numpy as np
import pandas as pd
D = pd.DataFrame(np.random.randn(4,4))#产生4*4随机矩阵
print(D.skew())#计算三阶矩
print(D.kurt())#计算三阶矩