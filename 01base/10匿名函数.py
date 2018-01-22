f = lambda s:s*s
print(f)
print(f(5))
def a(x,y):
    return lambda: x*x+y*y
b = a
print(map(a,(1,2)))