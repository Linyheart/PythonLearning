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

    def takefood(self):
        print("您的宠物开始进食，请不要打扰它~")
        time.sleep(1)
        print("您的宠物吃得正开心~")
        time.sleep(1)
        print("您的宠物快吃完啦！")
        time.sleep(1)
        print("您的宠物吃完啦！吃饱饱，有精神！")

    def sleep(self):
        print("您的宠物有点困了，要睡觉啦！")
        time.sleep(1)
        print("您的宠物睡得正香~")
        time.sleep(1)
        print("您的宠物还在梦里哟~")
        time.sleep(1)
        print("您的宠物睡醒啦！快抱抱它吧!")



class Cat(Pets):
    def __init__(self, feature, *args, **kwargs):
        self.feature = feature
        super(Dogs, self).__init__(*args, **kwargs)

    def smile(self):
        print('一只柴犬在朝着你笑~快摸摸他的头吧！')

    def hairLoss(self):
        print('你的柴犬掉毛啦！快快清理吧！')



"""
class Police(Person):
    # 此init方法可不写,一般显式写出，是因为需要对入参进行更多的“预处理”
    def __init__(self,*args,**kwargs):
        super(Police,self).__init__(*args,*kwargs)
 
    def attack(self,terrorist_person):
        if not isinstance(terrorist_person,Police):
            terrorist_person.health-=self.weapon
            return 'hit the target'
        else:
            raise AttackError('target is your partner')
 
 
class Terrorist(Person):
    def __init__(self,*args,**kwargs):
        super(Terrorist,self).__init__(*args,**kwargs)
 
    def attack(self,police_person):
        if not isinstance(police_person,Terrorist):
            police_person.health-=self.weapon
            return 'hit the target'
        else:
            raise AttackError('target is your partner')
"""
