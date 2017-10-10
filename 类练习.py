# -*- coding:utf-8 -*-
#写一个Person类实现其中方法和变量的简单调用
class Person(object):

    def __init__(self,name):
        self.name = name

    def eat(self):
        print "My name is %s,I'm eatting..."%self.name

me = Person("zdy")
me.name = "xxx"
me.eat()

class Student(Person):
    def __init__(self,stu_num,name):
        super(Student,self).__init__(name)
        self.stu_num = stu_num

    def study(self):
        print "My name is %s,stu_num is %s,I'm studying..."%(self.name,self.stu_num)

student = Student("04152017","zdy")
student.study()
student.eat()