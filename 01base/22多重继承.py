class Dog(object):
    def say(self):
        print('wang wang ---')
class Cat(object):
    def jump(self):
        print('jump jump ---')
class Son(Dog,Cat):
    pass

s = Son()
s.say()
s.jump()
