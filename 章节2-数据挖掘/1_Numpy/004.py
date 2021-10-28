import numpy as np
arr = np.random.randn(5, 4)  #正态分布的数据
print(arr.mean())
print(np.mean(arr))
print(arr.sum())

print(arr.mean(axis=1))
print(arr.sum(0))

arr = np.array([[0, 1 ,2], [3, 4, 5], [6, 7, 8]])
print(arr.cumsum(0))
print(arr.cumprod(1))
