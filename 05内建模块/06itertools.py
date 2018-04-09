import itertools


# count(n) 从n开始无限加1
s1 = itertools.count(2)
for s in s1:
    print(s)
    if s > 5:
        break

# cycle()会把传入的一个序列无限重复下去
s2 = itertools.cycle('ABC')
n2 = 1
for s in s2:
    print(s)
    n2 = n2 + 1
    if n2 > 5:
        break

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
s3 = itertools.repeat('GH')
n3 = 1
for s in s3:
    print(s)
    n3 = n3 + 1
    if n3 > 5:
        break

s3 = itertools.repeat('gh', 3)
for s in s3:
    print(s)

# takewhile()截取
s4 = itertools.count(1)
t4 = itertools.takewhile(lambda x: x < 5, s4)
print(t4)
print(list(t4))

# chain()可以把一组迭代对象串联起来
for c in itertools.chain('gao','huan'):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))