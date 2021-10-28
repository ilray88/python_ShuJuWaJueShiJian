#使用Python数组创建
import pandas as pd
import numpy as np

# DataFrame 简单应用
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = pd.DataFrame(data)
print(frame)

# 如果指定了列顺序，则DataFrame的列就会按照指定顺序进行排列。
print(pd.DataFrame(data, columns=['year', 'state', 'pop']))

# 跟原Series一样，如果传入的列在数据中找不到，就会产生NAN值。
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
print(frame2)
print(frame2.columns)

# 通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series。
print(frame2['state'])

# 返回的Series拥有原DataFrame相同的索引，且其name属性也已经被相应地设置好了。
print(frame2['year'])

# 列可以通过赋值的方式进行修改。例如，给那个空的“delt”列赋上一个标量值或一组值。
frame2['debt'] = 16.5
print(frame2)
frame2['debt'] = np.arange(5.)
print(frame2)

# 如果赋值的是一个Series，就会精确匹配DataFrame的索引，所有空位都将被填上缺失值。
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)

# 为不存在的列赋值会创建出一个新列。
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)

# 关键字del用于删除列。
del frame2['eastern']
print(frame2.columns)

# 将嵌套字典（也就是字典的字典）传给DataFrame，它就会被解释为：外层字典的键作为列，内层键则作为行索引；也可以对上述结果进行转置。
pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)
print(frame3.T)

# 如果设置了DataFrame的index和columns的name属性，则这些信息也会被显示出来。
frame3.index.name = 'year'
frame3.columns.name = 'state'
print(frame3)

# 跟Series一样，values属性也会以二维ndarray的形式返回DataFrame中的数据。
print(frame3.values)

# 如果DataFrame各列的数据类型不同，则数组的数据类型就会选用能兼容所有列的数据类型。
print(frame2.values)

# Index对象是不可修改的，因此用户不能对其进行修改。
obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index
print(index)
print(index[1:])