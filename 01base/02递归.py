#阶乘
def jc(n):
    if n == 1:
        return 1
    if n > 1:
        return n * jc(n-1)


#汉诺塔
def hnt(n, a, b, c):
    if n == 1:
        print(a + '--->' + c)
    if n > 1:
        hnt(n-1, a, c, b)
        hnt(1, a, b, c)
        hnt(n-1, b, a, c)


n = int(input('请输入汉诺塔的层数：'))
hnt(n, 'x', 'y', 'z')



print(jc(5))