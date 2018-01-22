class Student(object):
     def __init__(self,name,age):
         self.name = name
         self.age = age
     def get_name(self):
        return self.name
     def get_age(self):
        return self.age

c1 = Student('zs',25)
c2 = Student('ls',23)
print(c1.get_name())
print(c1.get_age())
print(c2.get_name())
print(c2.get_age())
