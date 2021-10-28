import numpy as np
arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8])
arr[5:8] = 12
print(arr)
arr_slice = arr[5:8]
arr_slice[1] = 12345
print(arr)
arr_slice[:] = 64
print(arr)
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d[0])
print(arr3d[0][1])
print(arr3d[0, 1])

