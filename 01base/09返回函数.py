def sum1(*args):
    s = 0
    for n in args:
        s = s + n
    return s
def sum2(*args):
    def sum3():
        s = 0
        for n in args:
            s = s + n
        return s
    return sum3
print(sum1(1, 2, 3))
f = sum2(1, 2, 3)
print(f)
print(f())
