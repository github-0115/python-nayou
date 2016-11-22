#!/user/bin/python
# -*- coding:utf-8 -*-


class Animal:
    '动物类'
    count = 0
    _countNum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.count += 1

    def run(self, speed):
        print str(self.age) + "岁的" + self.name + "奔跑速度为：" + str(speed) + "Km/h"


class Cat(Animal):
    def __init__(self, speed):
        self.speed = speed

    def eat(self):
        print '我爱吃鱼'

    def run(self, speed):
        print "cat" + str(self.speed)


if __name__ == '__main__':
    dog = Animal('dog', 5)
    dog.run(50)
    print dog.name + str(dog.age)
    dog.count = 5
    print dog.count
    print Animal.count
    Animal.count = 4
    print Animal.count
    print hasattr(dog, 'name')
    print hasattr(dog, 'speed')
    print getattr(dog, 'name')

    cat = Cat(20)
    cat.eat()
    setattr(cat, 'age', 2)
    setattr(cat, 'name', 'cat')
    cat.run(cat.speed)
    cat.run(cat.speed)
    print isinstance(cat,Animal)
