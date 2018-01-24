# student1
class Student1(object):
    pass
s1 = Student1()
s1.name = 'zs'
print(s1.name)

# student2
class Student2(object):
    def get_score(self):
        return self.__score
    def set_score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be int')
        if value < 0 or value > 100:
            raise ValueError('score must be 0-100')
        self.__score = value
s2 = Student2()
s2.set_score(20)
print(s2.get_score())
# print(s2.__score)

# student3
class Student3(object):
    @property
    def score(self):
        return self.__score

    @score.setter
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be int')
        if value < 0 or value > 100:
            raise ValueError('score must be 0-100')
        self.__score = value

s3 = Student3()
s3.__score = 22
print(s3.__score)

# Screen
class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def set_width(self, value):
        self.__width = value
    @property
    def height(self):
        return self.__width * 2
s5 = Screen()
s5.__width = 20
print(s5.__width)
# print(s5.height)

