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

# filter
print('-----filter------')
def f2(s):
    return s and s.strip()
print(' ' and ' '.strip())
print(f2(' '))


def is_odd(x):
    return x % 2 > 0
print(is_odd(3))
print(is_odd(4))

def odd(x):
    n = 1
    while True:
        n = n + 1
        yield 2 * n -3
        if n > x :
            break

print(odd)
print(odd(3))
print(list(odd(3)))

def ss(x):
    n = 1
    while n <= x:
        yield n
        n = n + 1

print(list(ss(10)))

print(list(filter(is_odd ,list(ss(20)))))


a1 = lambda x:x%2==0
print(a1(10))

def la(n):
    return lambda x:x % n > 1
b1 = la(3)
print(b1(6))
print(b1(7))
print(b1(8))

print("--------------获取素数------------------")
def odd():
    n = 1
    while True:
        n = n + 2
        yield n
def isOdd(n):
    return lambda x:x%n>0
def get():
    # yield 2
    it = odd()
    while True:
        n = next(it)
        yield n
        it = filter(isOdd(n),it)
for num in get():
    if num < 100:
        print(num)
    else:
        break
print("--------------获取回环数------------------")
def isHH(x):
    xStr = str(x)
    if len(xStr) == 1:
        return True
    y = 0
    while y < len(xStr)//2:
        if xStr[y] == xStr[-y - 1]:
            y = y + 1
        else:
            return False
    return True
def isHH2(x):
    return str(x) == str(x)[::-1]
def ss():
    s = num()
    while True:
        n = next(s)


print(isHH('123'))
print(isHH('123454321'))
print(list(filter(isHH,range(1000))))
print(list(filter(isHH2,range(1000))))

print('1234567'[::-1])
print('1234567'[::-2])
print('1234567'[::-3])
# sorted key 可以传入函数
print("--------------sorted------------------")
a = [36, 5, -12, 9, -21]
print(sorted(a))
print(sorted(a,key = abs))
b = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(b))
print(sorted(b,key = str.lower))
print(sorted(b,key = str.upper))
print(sorted(b,key = str.upper,reverse=True))
c = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def aa(x):
    return x[0]
def bb(x):
    return x[-1]
print(sorted(c,key=aa))
print(sorted(c,key=bb))