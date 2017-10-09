# -*- coding:utf-8 -*-
#打印所有文件内容的方法
def print_all(file):
    print file.read()

#重新定位到文件头部的方法
def rewind(file):
    file.seek(0)

#打印一行文件内容的方法
def print_a_line(line_count,file):
    print line_count,file.readline()

#打开文件
current_file = open("xxx.txt")

print "First let's print the whole file:"

print_all(current_file)

print "Now let's rewind,kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line+1
print_a_line(current_line,current_file)

current_line = current_line+1
print_a_line(current_line,current_file)