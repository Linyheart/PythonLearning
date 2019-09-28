"""
使用Pyhton面向对象为Pets进行建模
这里的Pets主要包括Cat, Dog两类，分别定义成两个类
所有的Pets都有name, color两个属性，所有的Pets都可以takeFood, sleep
Cat有type, pelage两个属性，所有的Cat都可以meow, scratch
Dog有type, size两个属性，所有的Dog都可以bark, bite
"""
import time


class Pets(object):

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return "这只宠物的名字是:%s , 颜色是:%s" % (self.name, self.color)

    def takefood(self):
        print("%s开始进食，请不要打扰它~" % self.name)
        time.sleep(0.5)
        print("%s吃得正开心~" % self.name)
        time.sleep(0.5)
        print("%s快吃完啦！" % self.name)
        time.sleep(0.5)
        print("%s吃完啦！吃饱饱，有精神！" % self.name)

    def sleep(self):
        print("%s有点困了，要睡觉啦！" % self.name)
        time.sleep(0.5)
        print("%s睡得正香~" % self.name)
        time.sleep(0.5)
        print("%s还在梦里哟~" % self.name)
        time.sleep(0.5)
        print("%s睡醒啦！快抱抱它吧!" % self.name)


class Cat(Pets):
    def __init__(self, name, color, types, pelage):
        self.name = name
        self.color = color
        self.type = types
        self.pelage = pelage
        super(Pets, self).__init__()

    def __str__(self):
        return "这只猫咪的名字是:%s , 颜色是:%s , 种类是:%s , 毛发情况是:%s" % (self.name, self.color, self.type, self.pelage)

    def meow(self):
        print("喵~喵~喵！")

    def scratch(self):
        print("%s生气地抓了你一下~" % self.name)


class Dog(Pets):
    def __init__(self, name, color, types, size):
        self.name = name
        self.color = color
        self.type = types
        self.size = size
        # super(Pets, self).__init__(*args, **kwargs)
        super(Pets, self).__init__()

    def __str__(self):
        return "这只狗狗的名字是:%s , 颜色是:%s , 种类是:%s , 大小是:%s" % (self.name, self.color, self.type, self.size)

    def bark(self):
        print("汪~汪~汪！")

    def bite(self):
        print("%s生气地咬了你一下~" % self.name)


if __name__ == '__main__':
  print("模块被直接执行!")
else:
    print("模块被导入！")