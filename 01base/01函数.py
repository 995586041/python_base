'''

Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

'''


'''位置参数'''

def m1(x):
    return x * x

def m2(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

'''
默认参数:有多个默认参数时，调用的时候，可以按顺序提供默认参数,当不按顺序提供部分默认参数时，需要把参数名写上;默认参数必须指向不变对象！
'''
def m3(x, n=2): #必选参数,默认参数
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
def m4(name, gender, age=6, city='bj'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

'''可变参数:允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple'''
def m5(numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)
def m6(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

'''关键字参数:允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict'''
def m7(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
'''命名关键字参数:命名关键字参数必须传入参数名，这和位置参数不同'''
def m8(name, age, *, city, job):
    print(name, age, city, job)

def person(name, age, *args, city, job):
    print(name, age, args, city, job)
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

# 运行函数
# m1(5)
# m2(2, 3)
# m3(5)
# m4('gh', 'F')
# m4('gh', 'F', 20)
# m4('gh', 'F', city='xa')
# m5([1, 2, 3])
# m5((1, 2, 3))
# m5({1, 2, 3})
# m6(1, 2, 3)
# nums = [1, 2, 3]
# m6(*nums)
# m6(*[1, 2, 3])
# m7('gh', '20')
# m7('gh', '20', gender='F')
# m7('gh', '20', gender='F', city='xa')
# # **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# # 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# m7('gh', '20', **extra)
m8('gh', '20', city='xa', job='IT')