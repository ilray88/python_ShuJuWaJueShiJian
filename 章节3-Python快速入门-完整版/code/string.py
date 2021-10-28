str1='Hello Python!'
str2="I'm learning python!"
str3='''How "are" you?
How do you do?'''
print(str1)
print(str2)
print(str3)

#将每一个字符串以分号进行连接
str4={"hello","world","hello","china"}
result1=";".join(str4)
print(result1)
#查找字符串是否以hello开头
str4="hello world"
print(str4.startswith("hello"))
#在字符串索引号为7的位置开始查找是否以ld结尾
print(str4.endswith("ld",7))
#用hi替换字符串中的hello
str5="hello world,hello China"
print(str5.replace("hello","hi"))
#统计字符串中单词hello的总个数
print(str5.count("hello"))
#查找字符串a所在的位置
str6="This is an apple,I will give you an apple."
print(str6.find("an"))
print(str6.index("an"))
#用'-'来分割字符串
a='123-345-468-698'
b=a.split('-')
print(b)
#去掉字符串中左右两边的空格
a1='   hello world    '
b1=a1.strip()
b2=a1.lstrip()
b3=a1.rstrip()
print(b1)
print(b2)
print(b3)
#字符串大小写转换
s='Where there is a will, There is a way'
s1=s.lower()#小写
s2=s.upper()#大写
s3=s.swapcase()#大小写互换
s4=s.capitalize()#首字母大写
s5=s.title()#只有首字母大写，其余为小写，
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
#字符串测试
print(s.isalnum()) #是否全是字母和数字，并至少有一个字符 
print(s.isalpha())#是否全是字母，并至少有一个字符 
print(s.isdigit()) #是否全是数字，并至少有一个字符 
print(s.isspace()) #是否全是空白字符，并至少有一个字符 
print(s.islower()) #S中的字母是否全是小写 
print(s.isupper()) #S中的字母是否便是大写 
print(s.istitle()) #S是否是首字母大写的
#字符串切片
st1 = 'hello python!'
print(st1[0],st1[-2]) 
print(st1[1:3],st1[1:],st1[:-1])
st2= 'abcdefghijklmnop'
print(st2[1:10:2])
print(st2[::2])
print(st2[::-1]) 
print(st2[::-2])