'''
定义:如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
'''

from collections import Iterable

# list
t1 = [1, 2, 3, 4, 5, 6, 7]
for num in t1:
    print(num)

# tuple
t2 = (1, 2, 3, 4, 5, 6, 7)
for num in t2:
    print(num)

# dict
t3 = {'a': 1, 'b': 2, 'c': 3}
for k in t3:
    print("key: " + k)
for v in t3.values():
    print("val: " + str(v))
for k, v in t3.items():
    print("key: " + k + ", val: " + str(v))

# str
for ch in 'abcd':
    print(ch)

# 判断对象是否可以迭代
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))

# enumerate函数可以把一个list变成索引-元素对
t4 = ['a', 'b', 'c']
for i, obj in enumerate(t4):
    print(i, obj)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)