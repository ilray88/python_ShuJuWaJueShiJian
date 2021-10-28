#代码6：展示了re.sub()进行字符串匹配替换。
import re
tel = "1522-3093-459 #这是一个#电话号码，含11位数字"
# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", tel)
print("电话号码是: ", num)
# 删除非数字(-)的字符串
num = re.sub(r'\D', "", tel)
print("电话号码是 : ", num)