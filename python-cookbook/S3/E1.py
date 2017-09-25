"""
第三章：数字日期和时间
"""

# 1、数字的四舍五入,round(number,ndigits)
# ndigits为保留位数
x = 12.3156
print(round(x, 1))  # 12.3
print(round(x, 2))  # 12.32
# ndigits可以为负数，表示个十百位
y = 123456
print(round(y,-1))  # 123450
print(round(y,-3))  # 123000

# 2、执行精确的浮点运算，使用decimal的Decimal类

# 3、格式化输出format(number,格式)
# 位置[<>^]width--左对齐、右对齐和居中，可选
number = 11112.3456
print(format(number,'>20'))     #              11112.3456
print(format(number,'^20'))     #       11112.3456
# [,]--表示千位逗号，可选
print(format(number,','))       # 11,112.3456
# [.digit] 小数点后有效位数
print(format(number,'.2f'))     # 11112.35
# e,E,f
print(format(number,'.2e'))     # 1.11e+04

# 4、不同进制的转换
# int转其他进制
print(bin(1234))    # 0b10011010010
print(oct(1234))    # 0o2322
print(hex(1234))    # 0x4d2
# 其他进制转int，使用int(number,进制)
print(int('0b10011010010',2))   # 1234
print(int('0x4d2',16))          # 1234

# 5、大整数和字节字符串的转换，使用int.from_bytes(),和 int.to_bytes()

# 6、负数的处理
# 构建负数：一是使用complex(real,imag),二是使用带有j的表达式
a = complex(2,4)
b = 3-2j
# 常用计算和普通数字一样，特殊计算需要使用到cmath模块
# 属性有real实数，imag虚数，共轭conjugate
print(a.real,a.imag,a.conjugate(),sep=',')      # 2.0,4.0,(2-4j)
print(a+b)      # (5+2j)
print(a-b)      # (-1+6j)
print(a*b)      # (14+8j)
# 特殊计算需要用到cmath模块
import cmath
c = cmath.sqrt(-1)
print(c)        # 1j
print(cmath.sin(a))     # 正弦(24.83130584894638-11.356612711218174j)

# 7、特殊的数字：无穷大inf，无穷小inf，和非数字nan
# 构建这些数字：使用float函数
a_inf = float('inf')
print(a_inf)        # inf
b_nan = float('nan')
print(b_nan)        # nan
# 所有nan的数都不相等，相等判断都是返回False
c_nan = float('nan')
print(b_nan==c_nan)     # False
# 判断是否无穷和是否非数字的唯一方法是使用math.isinf()和isnan()方法
import math
print(math.isinf(a_inf),math.isnan(b_nan),sep=', ')     # True, True

# 8、分数的运算
# 构建分数：使用fractions模块的Fraction类
from fractions import Fraction
a_f = Fraction(3,4)
b_f = Fraction(5,7)
print(a_f+b_f)      # 41/28
print(a_f-b_f)      # 1/28
# 属性：分子和分母的值
c_f = a_f * b_f
print(c_f.numerator)    # 15
print(c_f.denominator)  # 28
# 分数、浮点数的转换
print(float(c_f))       # 0.5357142857142857
x = 0.45
x_f = Fraction(*x.as_integer_ratio())
print(x_f)  # 8106479329266893/18014398509481984
# 由于计算机二进制原因，浮点数本身不精确，导致转换出来的分数错误，这里可以使用limit_denominator()函数限制分母大小
x_ff = x_f.limit_denominator(50)
print(x_ff)     # 9/20

# 9、大数据运算，使用numpy模块
# 10、矩阵和线性代数，使用numpy模块 （之后再学习）

# 11、随机数的使用，使用random模块，本质是确定性的伪随机数，如果要保证安全性，使用ssl模块
import random
values = [1,2,3,4,5,6,7,8]
# 在样本框中选择：选择1个样本
print(random.choice(values))   # 6
print(random.choice(values))   # 3
# 在样本框中选择多个
print(random.sample(values,2))  # [6, 4]
print(random.sample(values,3))  # [2, 6, 7]
# 打乱样本框
random.shuffle(values)
print(values)                   # [6, 7, 2, 1, 5, 4, 8, 3]
# 生产随机整数，浮点数，使用random.randint(), random.random()

# 12、日期处理使用datetime模块（后续学习）

