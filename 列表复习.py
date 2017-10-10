# -*- coding:utf-8 -*-
filename = "books.txt"
file = open(filename,'w')
#清空文件内容
file.truncate()

#定义一个书名的列表
book_name = ["白夜行","嫌疑人X的献身","解忧杂货店"]
#此处出现乱码，由于中文的原因
print book_name
print "列表的长度为:%d"%len(book_name)

#为确定列表内容将其写入文件
file.write("列表内容为：\n")
for bookname in book_name:
    file.write(bookname+"\n")

#打印分隔符
file.write("-"*10+"\n")

#取列表的最后一个元素并写入文件
#pop指出栈操作，会在取最后一个进入列表的元素的同时将该元素从列表删除
file.write("列表顶部的元素为：%s"%book_name.pop())
print "现在列表的长度为：%d"%len(book_name)

#打印分隔符
file.write("-"*10+"\n")

#给列表内添加元素
book_name.append("Android第一行代码")
file.write("此时列表内的元素为：\n")
for bookname in book_name:
    file.write(bookname+"\n")

#关闭文件
file.close()