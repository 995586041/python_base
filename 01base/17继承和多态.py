class Animal(object):
    def say(self):
        print('animal say')
class Dog(Animal):
    def say(self):
        print('dog say')
class Cow(Animal):
    def say(self):
        print('cow say')
class aa(object):
    def say(self):
        print('aa say')
class bb(object):
    def say1(self):
        print('bb say')


a1 = Animal()
a2 = Dog()
a3 = Cow()
a1.say()
a2.say()
a3.say()

print(isinstance(a1, Animal))
print(isinstance(a1, Dog))
print(isinstance(a2, Animal))
print(isinstance(a3, Animal))

def to_say(animal):
    animal.say()
    animal.say()

to_say(Animal())
to_say(Dog())
to_say(Cow())
to_say(aa())
to_say(bb())