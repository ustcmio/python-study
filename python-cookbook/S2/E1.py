"""
第二章：字符串和文本
"""

# 1、字符串分割：多种不同类型的分割符
# 分割符比较单一或者规范，可以使用string类型的split
stus_str1 = 'Tom, Jerry, Carl'
stus1 = stus_str1.split(', ')
print(stus1)  # ['Tom', 'Jerry', 'Carl']
# 分割符不规范或者多个，可以使用re.split(reg,str)
stus_str2 = 'Tom; Jerry,  Carl   Lily;Lilei'
import re

reg = r'[;,\s]\s*'
stus2 = re.split(reg, stus_str2)
print(stus2)  # ['Tom', 'Jerry', 'Carl', 'Lily', 'Lilei']
# 在正则表达式中使用()，可以保留分割符
reg2 = r'(;|,|\s)\s*'
stus3 = re.split(reg2, stus_str2)
print(stus3)  # ['Tom', ';', 'Jerry', ',', 'Carl', ' ', 'Lily', ';', 'Lilei']

# 2、字符串开头和结尾检测
# str类型的startswith()和endswith()方法
filename = 'S1E1.py'
print(filename.startswith('SE'))  # False
print(filename.endswith('.py'))  # True
# 当需要判断多个开头时，可以传入元祖类型
filenames = ['file.c', 'S1E1.py', 'word.doc', 'S2.py']
tup = ('.py', '.c')
print([filename.endswith(tup) for filename in filenames])  # [True, True, False, True]

# 3、使用操作系统底层的通配符来检测字符串，使用fnmatch()函数

# 4、使用正则表达式re模块来检测字符串

# 13、字符串对齐，ljust(size),rjust(size)和center(size)方法，普遍情况可以使用format格式化输出
hello = 'Hello World!!!'
print(hello.ljust(30))  # Hello World!!!
print(hello.rjust(30))  # Hello World!!!
print(hello.center(30))  # Hello World!!!

# 14、合并，拼接字符串
# 方案1：对象是iterable对象，比如列表等，使用join()函数
animals = ['dog', 'cat', 'bird', 'pig']
print(', '.join(animals))  # dog, cat, bird, pig
# 方案2：对于少量短字符串直接使用+号
# 注意：print输出可以同时输出多个字符串，不需要实现拼接，并且使用sep参数设定分隔
print(*animals, sep=":")  # dog:cat:bird:pig

# 18、字符串的令牌模式解析
# （1）定义令牌
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
EQ = r'?P<EQ>='
WS = r'?p<WS>\s+'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, EQ, WS]))
# (2) scanner匹配

