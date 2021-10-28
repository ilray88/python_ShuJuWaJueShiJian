
# coding=gbk
# ʹ�þ�������Ԥ���ʤ���
import time
start = time.perf_counter()

# �������ݼ�
import pandas as pd
file_name = r'basketball.csv'
data = pd.read_csv(file_name)
#print(data.head())  # ��ȡǰ5�����ݼ�
print(data.loc[:5])
#               Date Unnamed: 1       Visitor/Neutral  PTS         Home/Neutral  \.....
# 0  Tue Oct 29 2013  Box Score         Orlando Magic   87       Indiana Pacers
# 1  Tue Oct 29 2013  Box Score  Los Angeles Clippers  103   Los Angeles Lakers
# 2  Tue Oct 29 2013  Box Score         Chicago Bulls   95           Miami Heat
# 3  Wed Oct 30 2013  Box Score         Brooklyn Nets   94  Cleveland Cavaliers
# 4  Wed Oct 30 2013  Box Score         Atlanta Hawks  109     Dallas Mavericks
#print(data.shape)   # (1319, 8)
#print(data[data.duplicated()])  # Empty DataFrame û���ظ�Ԫ��

data = pd.read_csv(file_name, parse_dates= ['Date'])    #skiprows ���Ե�����
data.columns = ['Date','StartTime', 'Visitor Team', 'VisitorPts', 'Home Team', 'HomePts', 'Score Type','OT?','Attend.', 'Notes']
#print(data.head())  #��������ͷ
print(data.loc[:5])
#         Date Score Type          Visitor Team  VisitorPts  \��������
# 0 2013-10-29  Box Score         Orlando Magic          87
# 1 2013-10-29  Box Score  Los Angeles Clippers         103
# 2 2013-10-29  Box Score         Chicago Bulls          95
# 3 2013-10-30  Box Score         Brooklyn Nets          94
# 4 2013-10-30  Box Score         Atlanta Hawks         109
print('-----')

# ��ȡ������

# �ҳ���ʤ�����
data['HomeWin'] = data['VisitorPts'] < data['HomePts']
y_true = data['HomeWin'].values
print(y_true[:5])  # [ True  True  True  True  True] �� numpy ����
# print(data.head())

# ����2���������� �ֱ�������ֻ��ӵ���һ��������ʤ�����
# �����ֵ䣬����ϴα������
from collections import defaultdict

won_last = defaultdict(int)

data['HomeLastWin'] = None
data['VisitorLastWin'] = None  # �����д���ԭ����û�У�Ӧ��������2�У����������ѭ�����ܴ�����2��

for index, row in data.iterrows():
    home_team = row['Home Team']
    visitor_team = row['Visitor Team']  # ѭ������������
    row['HomeLastWin'] = won_last[home_team]
    row['VisitorLastWin'] = won_last[visitor_team]
    data.loc[index] = row  # ��������
    won_last[home_team] = row['HomeWin']  # �ж���һ���Ƿ��ʤ
    won_last[visitor_team] = not row['HomeWin']

print('----')
print(data.loc[20:25])
#              Home Team  HomePts  OT? Notes  HomeWin HomeLastWin VisitorLastWin
# 20      Boston Celtics       98  NaN   NaN    False       False          False
# 21       Brooklyn Nets      101  NaN   NaN     True       False          False
# 22   Charlotte Bobcats       90  NaN   NaN     True       False           True
# 23      Denver Nuggets       98  NaN   NaN    False       False          False
# 24     Houston Rockets      113  NaN   NaN     True        True           True
# 25  Los Angeles Lakers       85  NaN   NaN    False       False           True


won_last['jj'] = 12
dd = won_last['Indiana Pacers']  # defaultdict�����������ڣ����ֵ����key�����ڵ�������ʱ�����صĲ���keyError����һ��Ĭ��ֵ
print(dd)  # 0
print(won_last)  # defaultdict(<class 'int'>, {'Indiana Pacers': 0, 'jj': 12}) ���ص���defaultdict����

dataset = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(dataset)
for index, row in dataset.iterrows():
    print(index)  # 0, 1, 2 ��ӡ���к�
    print(row)  # ��ӡ���� 1�� 2�� 3 �е�ȫ��Ԫ��

# ʹ�þ�����
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(random_state=14)  # ����������ӣ�ʹ������֣������� ���ǻ��ǲ�ͬ��
X_previousWins = data[['HomeLastWin', 'VisitorLastWin']].values  # ʹ���´�����2��������Ϊ����

from sklearn.model_selection import cross_val_score  # ʹ �ý�����֤ģ��ƽ���÷�
import numpy as np

scores = cross_val_score(clf, X_previousWins, y_true, scoring='accuracy')
mean_score = np.mean(scores) * 100
print('the accuracy is %0.2f' % mean_score + '%')  # ׼ȷ��Ϊ    the accuracy is 57.47%


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
import numpy as np


#��ȡ2013������������
standings_filename= r'standings.csv'
standings = pd.read_csv(standings_filename)

print(standings.head())
#    Rk                   Team Overall  Home   Road      E      W     A     C  \....
# 0   1             Miami Heat   66-16  37-4  29-12  41-11   25-5  14-4  12-6
# 1   2  Oklahoma City Thunder   60-22  34-7  26-15   21-9  39-13   7-3   8-2
# 2   3      San Antonio Spurs   58-24  35-6  23-18   25-5  33-19   8-2   9-1
# 3   4         Denver Nuggets   57-25  38-3  19-22  19-11  38-14   5-5  10-0
# 4   5   Los Angeles Clippers   56-26  32-9  24-17   21-9  35-17   7-3   8-2
# print(standings.shape)  # (30, 24) ��30ֻ���

# ����һ��������ֵ�� ��������Ƿ�ȶ���������
data['HomeTeamRanksHigher'] = 0
for index, row in data.iterrows():
    home_team = row['Home Team']
    visitor_team = row['Visitor Team']
    # �Ƚ������� ��������ֵ
    home_rank = standings[standings['Team'] == home_team]['Rk'].values[0]
    visitor_rank = standings[standings['Team'] == visitor_team]['Rk'].values[0]
    row['HomeTeamRanksHigher'] = int(home_rank > visitor_rank)
    data.loc[index] = row

X_homehigher = data[['HomeLastWin', 'VisitorLastWin', 'HomeTeamRanksHigher']].values
clf1 = DecisionTreeClassifier(random_state=14)
scores = cross_val_score(clf1, X_homehigher, y_true, scoring='accuracy')
mean_score1 = np.mean(scores) *100
print('the new accuracy is %.2f'%mean_score1 + '%') #the new accuracy is 59.67%

# �ٴ����������� �Աȱ�����2����һ��2�ӱ����Ľ��
last_match_winner = defaultdict(int)
data['HomeTeamWonLast'] = 0
for index, row in data.iterrows():
    home_team = row['Home Team']
    visitor_team = row['Visitor Team']
    teams = tuple(sorted([home_team, visitor_team]))
    row['HomeTeamWonLast'] = 1 if last_match_winner[teams] == row['Home Team'] else 0
    data.loc[index] = row
    winner = row['Home Team'] if row['HomeWin'] else row['Visitor Team']
    last_match_winner[teams] = winner

X_lastwinner = data[['HomeTeamWonLast', 'HomeTeamRanksHigher']]
clf2 = DecisionTreeClassifier(random_state=14)
scores = cross_val_score(clf2, X_lastwinner, y_true, scoring='accuracy')
mean_score2 = np.mean(scores) *100
print('the accuracy is %.2f'%mean_score2 + '%') #  the accuracy is 57.85%

# ʹ��LabelEncoder ת�������ַ������͵Ķ���ת��������
from sklearn.preprocessing import LabelEncoder

encoding = LabelEncoder()
encoding.fit(data['Home Team'].values)  # ����������ת��������
home_teams = encoding.transform(data['Home Team'].values)
visitor_teams = encoding.transform(data['Visitor Team'].values)

X_teams = np.vstack([home_teams, visitor_teams]).T
from sklearn.preprocessing import OneHotEncoder

onehot = OneHotEncoder()
X_teams_expanded = onehot.fit_transform(X_teams).todense()
clf3 = DecisionTreeClassifier(random_state=14)
scores = cross_val_score(clf3, X_teams_expanded, y_true, scoring='accuracy')
mean_score3 = np.mean(scores) *100
print('the accuracy is %.2f'%mean_score3+'%')   #  the accuracy is 59.52%

print('----rf-----')
# ʹ�����ɭ�ֽ���Ԥ��
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(random_state = 14, n_jobs =-1)  #��õ��¾������Ĳ���
rf_scores = cross_val_score(rf, X_teams, y_true, scoring='accuracy')
mean_rf_score = np.mean(rf_scores) *100
print('the randforestclassifier accuracy is %.2f'%mean_rf_score+'%')    #the randforestclassifier accuracy is 58.38%

# ��ʹ�ü�������
print('ʹ�ö������')
X_all = np.hstack([X_homehigher, X_teams])
rf_clf2 = RandomForestClassifier(random_state = 14, n_jobs=-1)
rf_scores2 = cross_val_score(rf_clf2, X_all, y_true, scoring='accuracy')
mean_rf_score2 = np.mean(rf_scores2) *100
print('the accuracy is %.2f'%mean_rf_score2+'%')    # the accuracy is 57.62%

# �������� ʹ����������
from sklearn.model_selection import GridSearchCV

param_grid = {
    'max_features': [2, 3, 'auto'],
    'n_estimators': [100, 110, 120],
    'criterion': ['gini', 'entropy'],
    "min_samples_leaf": [2, 4, 6]
}
clf = RandomForestClassifier(random_state=14, n_jobs=-1)
grid = GridSearchCV(clf, param_grid)
grid.fit(X_all, y_true)
score = grid.best_score_ * 100
print('the accuracy is %.2f' % score + '%')  # the accuracy is 62.02%
something = str(grid.best_estimator_)
print(something)  # ������������ҵ������ģ��
print(grid.best_params_)  # ���������õĲ���
# the accuracy is 62.02%
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='entropy',
          max_depth=None, max_features=3, max_leaf_nodes=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=2, min_samples_split=2,
                       min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=-1,
                       oob_score=False, random_state=14, verbose=0, warm_start=False)
{'estimators': 100, 'criterion': 'entropy', 'max_features': 3, 'min_samples_leaf': 2}
# �����ѵ�ʱ�� �� 117.93s


end = time.perf_counter()
time = end - start
print('�����ѵ�ʱ�� �� %.2f' % time + 's')
















