import functools

def now():
    print('2018-01-22')

now()
print(now.__name__)
print('--------------------')

def log(func):
    def w(*args,**kw):
        print('log---> call %s():' % func.__name__ )
        return func(*args,**kw)
    return w


@log
def now2():
    print('2018-01-22')
now2()

print('--------------------')

def log2(text):
    def a(func):
        @functools.wraps(func)  #将函数包裹的函数名显示出来
        def b(*args,**kw):
            print('%s %s :' % (text,func.__name__))
            return func(*args,**kw)
        return b
    return a
@log2('log--->')
def now3():
    print('jjjjjjjjjjjj')
now3()
print(now2.__name__)
print(now3.__name__)

