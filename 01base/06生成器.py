g = (x * x for x in range(5))
print(g)
print(next(g))
print(next(g))
print(next(g))
print('----------------')

for n in g:
    print(n)

def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
fib1(5)
fib2(5)

for n in fib2(3):
    print(n)
    
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

