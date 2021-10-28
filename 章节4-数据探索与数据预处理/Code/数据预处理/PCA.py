# -!- coding: utf-8 -!-
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
A= np.random.rand(10,4)
pca=PCA()
pca.fit(A)
PCA(copy=True,n_components=None, whiten=False)
print(pca.components_ )#返回模型的各个特征向量