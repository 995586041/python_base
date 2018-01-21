
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
    

def tri(row):
    L = [1]
    while True:
        yield L
        L = [L[x] + L[x+1] for x in range(len(L)-1)]
        L.insert(0, 1)
        L.append(1)
        if len(L) > row:
            break

a = tri(5)
for b in a:
    print(b)

