# -*-coding:utf-8-*-
#创建一个个人信息的字典
person = {
    "name":"Zh.EastSun",
    "age":20,
    "stu_num":"04152017"
}

#输出字典信息
print person
#按键取相关数据
print "My name is %s"%person["name"]
print "I'm %d years old"%person["age"]
print "My student number is : %s"%person["stu_num"]
#添加相关信息
person["phone_num"] = "911"

print person

#删除相关信息
del person["phone_num"]

print person