print(type(123))
print(type('123'))
print(type(len))
print(type(len) == type(abs))

# dir
print(dir('123'))
print(len('123'))
print('123'.__len__())

class AA(object):
    def __init__(self):
        self.name = 'zs'
aa = AA()
print(hasattr(aa, 'name'))
print(aa.name)
print(hasattr(aa, 'age'))
print(getattr(aa,'age',404))
setattr(aa,'age',20)
print(aa.age)