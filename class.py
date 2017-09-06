#coding=utf-8
class Human(object):
    def __init__(self,name):
        self.__name = name
    def walk(self):
        print self.name+" is walking"
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name

human_a = Human("zdy")

#human_a.walk()

print human_a.get_name()

human_a.set_name("zh.EastSun")

print human_a.get_name()

class Man(Human):
    def __init__(self,name,has_wife):
        super(Man,self).__init__(name)
        self.__has_wife = has_wife
    def smoke(self):
        print "A man maybe smoke"
    def drink(self):
        print "A man maybe drink"
    def get_has_wife(self):
        return self.__has_wife

class Woman(Human):
    def __init__(self,name,has_husband):
        super(Woman,self).__init__(name)
        self.__has_husband = has_husband
    def shopping(self):
        print "A woman always go shopping."
    def make_up(self):
        print "A woman always make up."
    def get_has_husband(self):
        return self.__has_husband


man_zdy = Man("zdy","girlfriend")
man_zdy.smoke()
man_zdy.drink()
print "zdy has " + man_zdy.get_has_wife()

woman_xxx = Woman("xxx","boyfriend")
woman_xxx.shopping()
woman_xxx.make_up()
print "xxx has " + woman_xxx.get_has_husband()
