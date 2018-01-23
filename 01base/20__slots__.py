class Student(object):
    aa = 'aa'
    __bb = 'bb'


Student.cc = 'cc'

ss = Student()
print(ss.aa)
print(ss.cc)
# print(ss.__bb)
ss.bb = 'bb'
print(ss.bb)

from types import MethodType

# 给一个实例绑定的方法，对另一个实例是不起作用的
def set_age(self, age):
    self.age = age

ss.set_age = MethodType(set_age, ss) #给实例添加方法
ss.set_age(25)
print(ss.age)

sss = Student()
# print(sss.age)

def set_name(self, name):
    self.name = name
Student.set_name = set_name #给类添加方法
s1 = Student()
s1.set_name(11)
s2 = Student()
s2.set_name(22)
print(s1.name)
print(s2.name)

# 使用__slots__
# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class AA(object):
    __slots__ = ('name', 'age')
    # __slots__ = ('name', 'age', 'xx')

aa = AA()
aa.name = 'zs'
aa.age = 20
aa.xx = 'xx'
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class BB(AA):
     pass

bb = BB()
bb.name = 'sss'
