import  pandas as pd
import numpy as np
data = pd.DataFrame({'A':np.random.randint(1, 100, 10),
                     'B':np.random.randint(1, 100, 10),
                     'C':np.random.randint(1, 100, 10)})
print(data.corr())   # 计算pearson相关系数
print(data.corr('kendall'))     # Kendall Tau相关系数
print(data.corr('spearman'))     # spearman秩相关