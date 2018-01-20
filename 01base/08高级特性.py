# map
def f(x):
    return x * x
a = (1, 2, 3)
r1 = map(f, [1, 2, 3])
r2 = map(f, a)
print(list(r1))
print(list(r2))

# reduce: 传入的函数必须有两个参数, 传入的参数可以只有一个
from functools import reduce
def f1(x, y):
    return 10 * x + y
b = (1, 2, 3)
print(reduce(f1, [0]))
print(reduce(f1, [1]))
print(reduce(f1, [1, 2, 3]))
print(reduce(f1, b))


def f2(s):
    return s and s.strip()
# filter
print(' ' and ' '.strip())
print(f2(' '))
