L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-2])
print(L[-2:])
print(L[:])
L = list(range(100))
print(L)
# 前10个
print(L[:10])
# 后10个
print(L[-10:])
# 前11-20
print(L[10:20])
# 前10个数，每2个取一个
print(L[:10:2])
# 所有数，每10个取一个
print(L[::10])
# tuple
print((0, 1, 2, 3, 4, 5)[:3])
# str
print('abcdefg'[:3])