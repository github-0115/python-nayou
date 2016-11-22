#!/user/bin/python
# -*- coding:utf-8 -*-

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

if __name__ == '__main__':

    d = dict(name='Bob', age=20, score=88)
    print json.dumps(d)

    s = Student('Bob', 20, 88)

    print json.dumps(student2dict(s))

    print(json.dumps(s, default=lambda obj: obj.__dict__))


    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    print(json.loads(json_str, object_hook=dict2student))