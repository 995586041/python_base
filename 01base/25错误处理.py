def devide1():
    10/0

def devide2():
    try:
        10/0
    except ZeroDivisionError as e:
        print('零除错误')
    finally:
        print('------')

def devide3(num):
    if num %2 == 0:
        raise ValueError
    else:
        print('suc')


# devide1()
# devide2()
devide3(4)