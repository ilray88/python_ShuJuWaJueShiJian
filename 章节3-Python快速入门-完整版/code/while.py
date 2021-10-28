#代码1：展示了使用while循环实现计算100以内奇数的和。
sum = 0
x = 1
while x<=100:
    if x%2!=0:
        sum+=x;
    x+=1;
print(sum)


#1)while循环与continue语句一起使用实现1-10之间的偶数输出显示。
i = 1
while i < 10:   
    i += 1
    if i%2 > 0:  #非双数时跳过输出
        continue
print( i )#输出双数2、4、6、8、10

#2)while循环与break语句一起使用实现:使x不断减少，当x小于0.0001时终止循环。
x=10
count = 0 
while 1:
    count = count + 1
    x = x - 0.02*x
    if x< 0.0001:
        break
print (x,count)

