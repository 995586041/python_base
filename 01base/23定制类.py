class Student1(object):
    def __init__(self,name):
        self.name = name


class Student2(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '----------> (name,%s)' % self.name

    def __repr__(self):
        return '----------> (name,%s)' % self.name

    # 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
    def __getattr__(self, item):
        if item == 'age':
            return 32


print(Student1('gh'))
s1 = Student1('gh')
print(s1)
# print(s1.age)

print(Student2('gh'))
s2 = Student2('gh')
print(s2)
print(s2.age)


class Chain(object):
