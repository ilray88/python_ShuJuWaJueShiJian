#代码1：展示了使用for循环实现10的阶乘。
list=[1,2,3,4,5,6,7,8,9,10]
s = 1
for i in list:  #也可以使用for i in range(1,11): 
s *= i
print("The result is :",s)

#代码2：展示了使用for循环实现1-100之间被3整除的数的总和。
sum = 0
for i in range(1,101):
If i%3==0:
sum+= i
print("The number is :",sum)
