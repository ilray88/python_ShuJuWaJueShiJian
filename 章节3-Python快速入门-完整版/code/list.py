list1=[]
print(list1)
list2=[0,1,2]
print(list2)
list3=[“How”,”do”,”you”,”do”,”?”]
print(list3)
list4=[list2,4.35,6.24,8.42,list3]
print(list4)

 str="Hello Python"
 list5=list(str)
 list5

listA= ['Adam',95.5, 'Lisa',85, 'Bart',59]
listA[0]
listA[-1]
listA[-2]
listA[2]

listB=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
listB[1:5]
listB[6:10]
listB[1:]#默认步长为1 
listB[1:10:2] #步长为2
listB[1:10:3] #步长为3
listB[-3:-1]
listB[-3:] #包括序列结尾的元素，置空最后一个索引
listB[:] #复制整个序列

list6=[]
list6.append("hello")
 list1.extend([10,11,12])
 list1.insert(1,25)
 list6

list7=[1,2,3,4,5,6,7,8]
list7.remove(6)
list7
list=list7.pop()
list
list7
del list7[0]
list7

x = [1,2,3,4,5];
print(x)#修改前，输出列表元素内容
x[1]=0
print(x)#修改后，输出列表元素内容

#“+”操作符应用
str1='Hello'
str2=' Python'
str1+str2
n1=[1,2,3]
n2=[2,3,4]
n1+n2
str1+n1

#“*”操作符应用
[None]*6
str3='Python!'
str3*2
n3=[1,2]
n3*2
str3*n3

listC=[1,2,1,4,123,1]
listC
listC.count(1) 
listC.index(123) 
listC.reverse() 
listC
listC.sort() 
listC
listC.sort(reverse=True) 
listC
len(listC) 
max(listC)
min(listC)
