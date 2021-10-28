#1元组的创建
#方式1：使用小圆括号，即“()”
t1 = ('physics', 'chemistry', 1997, 2000)
t2 = (1, 2, 3, 4, 5 )
t3 ="a", "b", "c", "d"#逗号分隔一些值，元组自动创建完成
t4=()#空元组可以用没有包含内容的圆括号来表示
t5=(1,)#只含一个值的元组，必须加个逗号（,）
print(t1,t2,t3,t4,t5)

#方式2：使用tuple函数将一个序列转化为元组
t6=tuple([1,2,3,4,5,6])
t7=tuple("Hello Python")
t8=tuple((11,12,13,14,15))
t9=tuple(123)
print(t6,t7,t8,t9)

#元组的访问
t1 = ('root','chy','lxh')
t2= ('11','12','23')
print(t1[0])
print(t1[2:])
print(t1[::-1])
print(t1[:-1])
t2[0]=’00’#元组不可修改
#元组相加
t1 = ('root','chy','lxh')
t2= ('11','12','23')
t3=t1+t2#合并2个元组的元素为新元组的元素
t3

#元组相乘
t1 = ('root','chy','lxh')
t4=t1*3
t4
#成员检测
t1 = ('root','chy','lxh')
#判断元素在元组中
if 'chy' in t1:
    print("chy存在")
#判断元素不在元组中
if 'rhy' not in t1:
    print("rhy不存在")

#元组的常用操作函数
tup = (19, 23, 45,19,32)
#获取元组的长度
 len(tup)
#获取元组中最大值
max( tup)
#获取元组中最小值
min(tup)
#查询元素的索引
index = tup.index(23)
print(index) 