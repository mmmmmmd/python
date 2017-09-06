#coding=utf-8


#字符串的查找
#find方法，若字符串中有所查找的字符，那么返回
#该字符的下标，若不存在则返回-1     例：

String = "abc"
print String.find('a')
print String.find('b')
print String.find('d')


#字符串的分割
#split方法，以参数为分隔符将字符串进行分割
#返回值为分割后的字符串         例：

String = "aa12bb12cc12dd"
print String.split("12")

#字符串的大小写转化
#upper方法，将调用此方法的字符串转换为大写形式
#lower方法，将调用此方法的字符串转换为小写形式   例:

String = "abc"
print String.upper()

String = "SABER"
print String.lower()


#字符串的截取
#类似于数组的截取字符串名[开始的下标：结束的下标]
#python的下标值可以取负数，负数代表的意思就是从
#后向前取            例：

String = "123456"
print String
print String[1:3]
print String[:3]
print String[3:]
print String[:-2]


#字符串的追加
#第一个字符串+第二个字符串       例：
s = "abc"
t = "def"

print s+t
print t+s



#字符串的替换
#replace方法，将字符串中第一个参数替换为第二个参数  例：

String = "1,2,3"

print String.replace(",","#")
