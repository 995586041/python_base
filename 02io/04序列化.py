import pickle

#pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象

d = dict(name='zs', age=12, weight=75)
print(pickle.dumps(d))
f = open('aa.text','wb')
pickle.dump(d,f)
f.close()
f2 = open('aa.text', 'rb')
print(pickle.load(f2))
f2.close()

import json

# 用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
d2 = dict(name='zs', age=12, weight=75)
print(json.dumps(d2))
d3 = '{"name": "zs", "age": 12, "weight": 75}'
print(json.loads(d3))


import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class
print(json.dumps(s, default=lambda object:object.__dict__))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook=dict2student))