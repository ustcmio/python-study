"""
第一章：数据结构和算法
"""

# 1、通过简单赋值来解压
# 赋值变量个数要和列表元素数量相等
pos = (1, 2, 3)
x, y, z = pos
print(x, y, z)  # 1 2 3

# 可以解压的包括元祖、列表、迭代器、生成器，字符串等
# 可以使用下划线_来占位，代替不想要的元素,
info = ['name', 'age', 'addr', 'company']
name, age, _, _ = info

# 2、可以使用*加变量名来接受不定个数的元素
prices = [21, 3, 5, 7, 98, 43, 5, 7]
mon, *day, sun = prices
print(day)  # [3, 5, 7, 98, 43, 5]

# 同样可以使用下划线加星号*_来占位，替代不需要的多个元素
record = ['name', 'age', 'addr', ('tel1', 'tel2', 'housenumber')]
name, *_, (*_, housenumber) = record
print(name, housenumber)  # name housenumber

# 3、collections模块的deque函数，构建一个队列
# 1、双向操作，appendleft(),2、固定长度的队列，先进先出
from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)  # deque([1, 2, 3])
q.appendleft(4)
print(q)  # deque([4, 1, 2, 3])

l = deque(maxlen=3)
l.append(1)
l.append(2)
l.append(3)
print(l)  # deque([1, 2, 3], maxlen=3)
l.append(4)
print(l)  # deque([2, 3, 4], maxlen=3)

# 4、最大或者最小的N个元素
# 使用heapq模块的nlargest(),和nsmallst()函数
nums = [1, 5, 2, 4, 45, 12, 3, -2, 51, -4]
import heapq

print(heapq.nlargest(3, nums))  # [51, 45, 12]
print(heapq.nsmallest(3, nums))  # [-4, -2, 1]


# 同样可以接收key参数，用来比较更为复杂的数据结构
def getScore(student):
    return student['score']


students = [
    {'name': 'Tom', 'age': 12, 'score': 97.5},
    {'name': 'Jerry', 'age': 10, 'score': 91.2},
    {'name': 'Carl', 'age': 14, 'score': 95.2},
    {'name': 'Edward', 'age': 12, 'score': 87.5}
]

print(heapq.nlargest(2, students,
                     key=getScore))  # [{'name': 'Tom', 'score': 97.5, 'age': 12},{'name': 'Carl', 'score': 95.2, 'age': 14}]

# heapq模块的实质是（1）通过heapify函数，将列表的最小元素调整到0位置，（2）然后通过heappop()函数取出
heapq.heapify(nums)  #
print(nums)  # [-4, -2, 2, 1, 5, 12, 3, 4, 51, 45]
print(heapq.heappop(nums))  # -4
print(nums)  # [-2, 1, 2, 4, 5, 12, 3, 45, 51]
print(heapq.heappop(nums))  # -2
print(nums)  # [1, 4, 2, 45, 5, 12, 3, 51]
print(heapq.heappop(nums))  # 1
print(nums)  # [2, 4, 3, 45, 5, 12, 51]

# 5、元素的优先级
q = []
heapq.heappush(q, (-5, 0, 'first'))
heapq.heappush(q, (2, 1, 'second'))
heapq.heappush(q, (-1, 2, 'third'))
heapq.heappush(q, (-5, 3, 'four'))
print([s[-1] for s in q])  # ['first', 'four', 'third', 'second']

# 6、多值映射字典，可以使用defaultdict
d = {
    'a': [1, 3, 4],
    'b': [2, 5, 6]
}

# 7、字典排序 OrderedDict
