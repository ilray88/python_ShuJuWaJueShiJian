#1）匹配查询函数
#代码1：展示了match函数的应用：
import re
print(re.match('www', 'www.baidu.com').span()) #在起始位置匹配
print(re.match('com', 'www.baidu.com'))  #不在起始位置匹配

#代码2：展示了group()获取匹配对象。
import re 
line = "Cats are smarter than dogs"
match= re.match( r'(.*) are (.*?) .*', line, re.M|re.I) 
if match:
   print "match.group() : ", matchObj.group()
   print "match.group(1) : ", matchObj.group(1)
   print "match.group(2) : ", matchObj.group(2)
else:
   print "No match!!"

#(2)re.search()

代码3：展示了search函数的应用：
import re
print(re.search('www', 'www.baidu.com').span()) #在起始位置匹配
print(re.search('com', 'www.baidu.com').span()) #不在起始位置匹配

#代码4：展示了group()获取匹配对象。
import re 
line = "Cats are smarter than dogs"
match= re.match( r'(.*) are (.*?) .*', line, re.M|re.I) 
search = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
 if search:
   print "search.group() : ", search.group()
   print "search.group(1) : ", search.group(1)
   print "search.group(2) : ", search.group(2)
else:
   print "Nothing found!!"

#(3)re.findall()

#代码5：展示了findall与compile方法的使用
import re 
pattern = re.compile(r'\d+') #查找数字
result1 = pattern.findall('The world 123 the people 456 good')
result2 = pattern.findall('The world 123 the people 456 good', 0, 10) 
print(result1)
print(result2)

#匹配替换函数
 
#代码6：展示了re.sub()进行字符串匹配替换。
import re 
tel = "1522-3093-459 #这是一个#电话号码，含11位数字"
# 删除字符串中的 Python注释 
num = re.sub(r'#.*$', "", tel)
print("电话号码是: ", num)
# 删除非数字(-)的字符串 
num = re.sub(r'\D', "", tel)
print("电话号码是 : ", num)

#3）匹配分割函数

#代码7：展示了该方法进行字符串分割的应用。
import re
print(re.split('\W+', 'goodjob, goodjob, goodjob.'))
print(re.split('(\W+)', 'goodjob,goodjob, goodjob.')) 
print(re.split('\W+', ' goodjob, goodjob, goodjob.', 1)) 
print(re.split('a*', 'hello world'))#对于一个找不到匹配的字符串而言，split不会对其作出分割
