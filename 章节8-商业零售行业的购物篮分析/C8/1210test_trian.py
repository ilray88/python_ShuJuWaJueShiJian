##随机森林
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import learning_curve
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

bf = pd.read_csv("BlackFriday.csv", header = 'infer')
plt.rcParams['font.sans-serif']=['SimSun']

# 检查数据中是否有缺失值，以下两种方式均可
# Flase:对应特征的特征值中无缺失值
# True：有缺失值
print(bf.isnull().any())
#print(pd.isnan(bf).any())

# 查看缺失值记录
train_null = pd.isnull(bf)
train_null = bf[train_null == True]
print(train_null)

# 缺失值处理，以下两种方式均可
# 删除包含缺失值的行
bf.dropna(inplace=True)
# 缺失值填充
bf.fillna('100')

# 检查是否包含无穷数据
# False:包含
# True:不包含
#print(np.isfinite(bf).all())
# False:不包含
# True:包含
#print(np.isinf(bf).all())

# 数据处理
#train_inf = np.isinf(bf)
#bf[train_inf] = 0
# 分别将 User_ID 和 Product_ID 的不同的字符的离散属性值，用整数表示
le_UID = LabelEncoder()
bf['User_ID'] = le_UID.fit_transform(bf['User_ID'])
le_PID = LabelEncoder()
bf['Product_ID'] = le_PID.fit_transform(bf['Product_ID'])

# 将性别转化为数字表示， Female: 0；Male: 1
bf['Gender'] = np.where(bf['Gender']=='M',1,0)
# 对年龄、居住城市、居住时间进行one-hot编码
bf_Age = pd.get_dummies(bf.Age)
bf_CC = pd.get_dummies(bf.City_Category)
bf_SICY = pd.get_dummies(bf.Stay_In_Current_City_Years)

#替换 bf 中对应的列
bf_encoded = pd.concat([bf,bf_Age,bf_CC,bf_SICY],axis=1)
bf_encoded.drop(['Age','City_Category','Stay_In_Current_City_Years'],axis=1,inplace=True)
print(bf_encoded.head(5))
df_frac =bf_encoded.sample(frac=0.02,random_state=100)
X = df_frac.drop(['Purchase'], axis=1)
y = df_frac['Purchase']

# train_test_split函数用于将矩阵随机划分为训练子集和测试子集，并返回划分好的训练集测试集样本和训练集测试集标签
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=100)

#针对每一个特征维度,进行去均值和方差归一化
scaler = StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
# 交叉验证cv:默认=3，评分函数scoring：neg_mean_squared_error
#param_test1 = {'n_estimators':[1,3,10,30,90,100,110,150]}
param_test1 = {'n_estimators':[1,3,10,30,90,100,110,150,300]}
#param_test1 = {'n_estimators':[1,3,10,30,90,100,110,150,300,330]}
grid_rf = GridSearchCV(RandomForestRegressor(),param_grid=param_test1,cv=3
,scoring='neg_mean_squared_error').fit(X_train_scaled,y_train)
# 画出 交叉验证的 均方根误差 (RMSE)得分
plt.figure()
plt.plot(list(param_test1.values())[0],(-1*grid_rf.cv_results_['mean_test_score'])**0.5)
plt.xlabel('Number of trees')
plt.grid()
plt.ylabel('3-fold CV RMSE')
plt.show()
print('Best parameter: {}'.format(grid_rf.best_params_))
print('Best score: {:.2f}'.format((-1*grid_rf.best_score_)**0.5))
train_sizes, train_scores, test_scores = learning_curve(RandomForestRegressor
(max_depth=13, min_samples_split=50,n_estimators=110), X_train_scaled, y_train, cv=3,
 scoring='neg_mean_squared_error')
#均值归一化
train_scores = (-1*train_scores)**0.5
test_scores = (-1*test_scores)**0.5
train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)
# 画出得分曲线
plt.figure()
plt.plot(train_sizes,test_scores_mean,label='test',linewidth=5)
plt.plot(train_sizes,train_scores_mean,label='train',linewidth=1)
# 波动范围：[平均值-标准差,平均值+标准差]
#plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.3,color="g")
#plt.fill_between(train_sizes, test_scores_mean - test_scores_std,test_scores_mean + test_scores_std, alpha=0.3, color="b")
plt.grid()
plt.xlabel('样本数量')
plt.ylabel('RMSE')
plt.legend()
plt.show()
