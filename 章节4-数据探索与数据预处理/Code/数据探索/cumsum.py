import pandas as pd
D=pd.Series(range(0, 5)) #构造Series， 内容为0～19共20个整数
print(D.cumsum()) #求出出前n项和
print(D.rolling(2).sum())