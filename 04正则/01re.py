'''
\d 数字  \w 字母或者数字  \s 空白字符 . 任意字符
* 0个或多个字符  + 至少一个字符  {n} n个字符  {n,m} n-m个字符
[a-zA-Z]  A|B  ^ 行开头  $ 行结尾
'''

import re

print(re.match(r'\d{3}\-\d{5}','010-12345'))
print(re.match(r'\d{3}\-\d{5}','010-qqq'))

# 切分字符串
str1 = 'a  b c  d'
print(re.split(r'[\s,]+', str1))

# 分组 ^(\d{3})-(\d{3,8})$分别定义了两个组
m = re.match(r'(\d{3}\-\d{5})','010-12345')
print(m)
print(m.group(0))
# print(m.group(1))
print(m.groups())

str2 = '11:22:33'
m2 = re.match(r'(\d+):(\d+):\d+', str2)
print(m2.groups())

# 贪婪匹配
print('----贪婪匹配---')
str3 = '1100'
m3 = re.match(r'(\d+)(0*)', str3)
print(m3.groups())
m3 = re.match(r'(\d+?)(0*)', str3)
print(m3.groups())
m3 = re.match(r'^(\d+?)(0*)$', str3)
print(m3.groups())

# 编译 如果一个正则表达式要重复使用几千次，出于效率的考虑，可以预编译该正则表达式
str4 = '11:aa:$$'
m4 = re.compile(r'^(\d+):(aa):(\$\$)$')
print(m4.match(str4))
print(m4.match(str4).groups())
