# __a 私有变量,不可被访问 __a__ 特殊变量,可被访问
class Person(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age__ = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age__
    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        self.__age__ = age


p1 = Person('zs', 23)
print(p1)
print(p1.__age__)
print(p1.get_name())
print(p1.__name)
p2 = Person('ls', 20)