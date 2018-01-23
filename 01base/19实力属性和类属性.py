class Student(object):
    name = 'zs'
    # def __init__(self,name):
    #     self.name = name


s = Student()
print(Student.name)
print(s.name)

s.name = 'ls'
print(Student.name)
print(s.name)

del s.name
print(Student.name)
print(s.name)


