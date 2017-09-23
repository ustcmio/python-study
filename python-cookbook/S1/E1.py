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
# 会按照插入的顺序来排序

# 8、字典运算
# 最大max()、最小min()、排序sorted()运算字典时，针对的健
d1 = {'Tom': 98.5,
      'Jerry': 88.5,
      'Zard': 90.5,
      'Carl': 94.5}

print(max(d1))  # Zard
print(min(d1))  # Carl
print(sorted(d1))  # ['Carl','Jerry','Tom','Zard']

# 要操作值，一种方法：传入key参数，另一种方法zip()函数，使键值互换
print(max(zip(d1.values(), d1.keys())))  # (98.5, 'Tom')
print(min(zip(d1.values(), d1.keys())))  # (88.5, 'Jerry')
print(sorted(zip(d1.values(), d1.keys())))  # [(88.5, 'Jerry'), (90.5, 'Zard'), (94.5, 'Carl'), (98.5, 'Tom')]
# zip()函数生成的是zip对象，只能使用一次
zip_object = zip(d1.values(), d1.keys())
print(max(zip_object))  # (98.5, 'Tom')
# print(min(zip_object))  # ValueError: min() arg is en empty sequence

# 9、使用集合的概念在处理字典的差异,但是并不能直接用于字典，而是用于keys(),values(),items(),返回的是set类型
d2 = {'x': 1, 'y': 5, 'z': 3, 'k': 2}
d3 = {'y': 5, 'z': 4, 'k': 1}
# 并集：获取字典相同元素
print(d2.keys() & d3.keys())  # {'y', 'z', 'k'}
print(d2.items() & d3.items())  # {('y', 5)}
# 差集：排除掉相同的元素，可以用于过滤
print(d2.items() - d3.items())  # {('x', 1), ('z', 3), ('k', 2)}
# 实现字典过滤掉特定的健，比如d2过滤掉y和z
d2_result = {k: d2[k] for k in d2.keys() - {'y', 'z'}}
print(d2_result)  # {'k': 2, 'x': 1}


# 10、保持原有顺序，删除掉序列中的相同元素
# 使用生成器，构建一个集合，将不再集合中的元素yield，并添加进集合，在集合中的元素必定之前yield过，即为重复元素
def dedupe(items):
    s = set()  # 构建一个集合，用于标记曾经yield过的元素
    for item in items:  # 遍历序列中的所有元素
        if item not in s:  # 如果不在s中，即未曾yield过，非重复元素
            yield item
            s.add(item)


nums = [1, 4, 2, 7, 5, 2, 6, 4, 3, 5, 7, 9]
nums_pro = list(dedupe(nums))
print(nums_pro)  # [1, 4, 2, 7, 5, 6, 3, 9]


# 如果序列中的元素不可比较，即不是hashable类型，则可以传入key函数，返回指定的可比较类型元素
def dedupe_(items, key=None):
    s = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in s:
            yield item
            s.add(val)


pos = [{'x': 1, 'y': 2}, {'x': 2, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]


def func(item):
    return item['x'], item['y']


pos_pro = list(dedupe_(pos, key=func))
print(pos_pro)  # [{'y': 2, 'x': 1}, {'y': 3, 'x': 2}, {'y': 4, 'x': 2}]

# 11、切片对象的使用slice()
a = slice(2, 6, 1)  # 构造slice有三个参数start,stop,step,step可以省略
# 切片可以用在所有能使用的地方
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(items[a])  # [3, 4, 5, 6]
items[a] = ['a', 'b']
print(items)  # [1, 2, 'a', 'b', 7, 8, 9, 10]
del items[a]
print(items)  # [1, 2, 9, 10]

# 12、序列重复元素的计数，使用collections模块的Counter类，序列元素必须是可比较类型，即hashable类型
from collections import Counter

works = ['book', 'work', 'study', 'work', 'book', 'foot', 'work']
works_counter = Counter(works)
print(works_counter)  # Counter({'work': 3, 'book': 2, 'foot': 1, 'study': 1})
# Counter 实质是dict类型
print(isinstance(works_counter, dict))  # True
# update(items) 方法对更多序列计数
moreworks = ['book', 'study', 'book']
works_counter.update(moreworks)
print(works_counter)  # Counter({'book': 4, 'work': 3, 'study': 2, 'foot': 1})
# Counter对象可以使用简单的加减
a_counter = Counter(works)
b_counter = Counter(moreworks)
print(a_counter + b_counter)  # Counter({'book': 4, 'work': 3, 'study': 2, 'foot': 1})

# 13、字典列表的不同字段的处理，比如按照不同的字段排序
from operator import itemgetter

students = [
    {'name': 'Tom', 'age': 15, 'score': 91.5},
    {'name': 'Bell', 'age': 14, 'score': 91.5},
    {'name': 'Carl', 'age': 12, 'score': 88.5},
    {'name': 'Jerry', 'age': 12, 'score': 95.5}
]

students_sorted = sorted(students, key=itemgetter('score', 'name'))
print(students_sorted)
# [{'age': 12, 'name': 'Carl', 'score': 88.5},
#  {'age': 14, 'name': 'Bell', 'score': 91.5},
#  {'age': 15, 'name': 'Tom', 'score': 91.5},
#  {'age': 12, 'name': 'Jerry', 'score': 95.5}]

student_max_score = max(students, key=itemgetter('score'))
print(student_max_score)  # {'name': 'Jerry', 'score': 95.5, 'age': 12}

# 14、关键字key的使用，传入一个可以callable的函数，用于返回可比较类型的元素

# 15、字典序列，按照某个字段进行分组，itertools模块的groupby()函数，前提：已经按照该字段排序
stus_school = [
    {'name': 'Tom', 'age': 15, 'school': 'a.collage'},
    {'name': 'Jerry', 'age': 14, 'school': 'c.collage'},
    {'name': 'Carl', 'age': 15, 'school': 'a.collage'},
    {'name': 'Bell', 'age': 12, 'school': 'b.collage'},
    {'name': 'Karl', 'age': 11, 'school': 'c.collage'}
]
from itertools import groupby

stus_school.sort(key=itemgetter('school'))
for school, stus in groupby(stus_school, key=itemgetter('school')):
    print(school)
    for stu in stus:
        print(stu)
# a.collage
# {'school': 'a.collage', 'name': 'Tom', 'age': 15}
# {'school': 'a.collage', 'name': 'Carl', 'age': 15}
# b.collage
# {'school': 'b.collage', 'name': 'Bell', 'age': 12}
# c.collage
# {'school': 'c.collage', 'name': 'Jerry', 'age': 14}
# {'school': 'c.collage', 'name': 'Karl', 'age': 11}

# 16、列表元素的过滤
mylist = [1, -3, 5, 4, -2, 6, -2, -5, 3, 5, 7]  # 需要过滤其中的负数
# 方案1：列表表达式
mylist1 = [i for i in mylist if i > 0]
print(mylist1)  # [1, 5, 4, 6, 3, 5, 7]


# 方案2：filter(func，list)内建函数，接收两个参数list为过滤前的列表，func为过滤判断
def func(item):
    if item > 0:
        return True
    else:
        return False


mylist2 = list(filter(func, mylist))
print(mylist2)  # [1, 5, 4, 6, 3, 5, 7]
# 方案3：使用itertools模块中的compress(list，Boolean_list)函数,Boolean_list中对应True的保留，False的被过滤
from itertools import compress

boolean_list = [i > 0 for i in mylist]
print(boolean_list)
mylist3 = list(compress(mylist, boolean_list))  # [True, False, True, True, False, True, False, False, True, True, True]
print(mylist3)  # [1, 5, 4, 6, 3, 5, 7]
# 除了可以过滤，还可以指定元素替换，比如大于零的都替换为0
mylist4 = [i if i < 0 else 0 for i in mylist]
print(mylist4)  # [0, -3, 0, 0, -2, 0, -2, -5, 0, 0, 0]

# 17、从字典中，抽取指定字段的子集
stus = {
    'Tom': 98.5, 'Jerry': 95.2, 'Carl': 88.5
}
# 抽取分数高于90分的学生
stus_by_score = {name: score for name, score in stus.items() if score > 90}
print(stus_by_score)  # {'Jerry': 95.2, 'Tom': 98.5}
# 抽取出Tom和Carl
stus_by_name = {name: stus[name] for name in stus.keys() & {'Tom', 'Carl'}}  # 集合的并集
print(stus_by_name)  # {'Carl': 88.5, 'Tom': 98.5}

# 18、映射名称到序列元素，使用namedtuple
# （1）命名元祖，本质是元祖，只是为元祖的每个元素进行了命名
from collections import namedtuple

Pos = namedtuple('Pos', ['x', 'y', 'z'])
point_pos = Pos(1, 2, 3)
print(isinstance(point_pos, tuple))  # True
# 可以通过下标或者命名的名称访问
print(point_pos[0], point_pos[2])  # 1 3
print(point_pos.x, point_pos.z)  # 1 3
# 可以用来简单的代替字典
print(point_pos)  # Pos(x=1, y=2, z=3)
# 但是本质是元祖，不可以直接修改值
# point_pos.x = 4  # AttributeError: can't set attribute
# 如果真的要修改，可以使用_replace()方法
point_pos = point_pos._replace(x=4)  # 实际是新建了一个namedtuple
print(point_pos)  # Pos(x=4, y=2, z=3)

# 19、生成器表达式，用括号包裹

# 20、字典的合并
# 方案：使用collections模块的ChainMap类，本质不生成新字典，而是建立两个字典的关联列表
from collections import ChainMap
dict1 = {'x': 2, 'y': 3}
dict2 = {'y': 4, 'z': 5}
c = ChainMap(dict1,dict2)
print(c)    # ChainMap({'x': 2, 'y': 3}, {'z': 5, 'y': 4})
# 相同字段，返回第一个字典的值
print(c['y'])    # 3
# 修改时，会同步修改第一个字典，不能修改第二个字典
c['y'] = 0
print(c)   # ChainMap({'y': 0, 'x': 2}, {'y': 4, 'z': 5})
print(dict1)    # {'y': 0, 'x': 2}
# del c['z']   # KeyError: "Key not found in the first mapping: 'z'" z这个字段不存在

