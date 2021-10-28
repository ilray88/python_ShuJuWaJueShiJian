#1.字典的创建
dict1 = {'Alice': 23, 'Beth': 24, 'Cecil': 22}
dict2 = {'a' : 'apple', 'b' : 'banana', 'g' : 'grape', 'o' : 'orange'}
dict3 = {'001' :{'Alice','male',23}, '002' : {'Beth','female',24}', '003' : {'Cecil','male',22}}
dict1
dict2
dict3
#用dict()通过关键字的参数来创建字典
dict4 = dict(Alice=23, Beth=24, Cecil=22)
dict5 = dict(a = 'apple', b= 'banana', g = 'grape', o ='orange')
dict6 = dict(A ={'Alice','male',23}, B= {'Beth','female',24}, C= {'Cecil','male',22})
dict4
dict5
dict6

#2.字典元素的访问
#字典通过键索引与get()方法实现元素的访问与获取。
dict4['Alice']
dict5['a']
dict6['A']
dict6.get('B')

#字典也可以通过keys(),values(),items()等方法来访问字典中的所有键，值或键值对。

dict6.keys()
dict6.values()
dict6.items()

#3.字典元素的添加
#一般通过setdefault()，update()，以及键索引三种方法实现向字典添加元素。
#（1）setdefault方法通过接收表示键值对的两个参数向字典中添加新元素。
dict4.setdefault('Betty', 36)
dict4

#（2）update方法通过接收一个字典对象向字典中添加新元素
dict4.update({'Jack':26})
dict4

#（3）键索引方法主要通过给原始字典中未指定的键添加值，而实现向字典中添加新元素
dict4['Rose']=39
dict4

#4.字典元素的修改
#一般主要通过update()与建索引的方法实现对字典中的元素进行修改。
dict4.update({'Jack':16})
dict4
dict4['Betty']=38
dict4

#5.字典元素的删除
#一般可以使用pop,popitem以及clear方法实现字典中元素的删除操作。例如：
dict4.pop('Jack')
dict4
dict4.popitem()
dict4
dict4.clear()
dict4