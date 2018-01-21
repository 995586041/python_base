t1 = list(range(1,10))
print(t1)
t2 = [x * x for x in range(10)]
print(t2)
t3 = [(x + x * 2) for x in range(10)]
print(t3)
t4 = [x * 2 for x in range(10) if x % 2 == 0]
print(t4)
t5 = [m + n for m in 'ABC' for n in 'abc']
print(t5)

import os
t6 = [d for d in os.listdir('.')]
print(t6)

dic = {'A':'a', 'B':'b', 'C':'c'}
t7 = [k + '=' + v for k, v in dic.items()]
print(t7)

L = ['Hello', 'World', 'IBM', 'Apple']
print([ x.lower()  for x in L ])