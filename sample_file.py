# -*- coding: utf-8 -*-
filename = raw_input("Please input the filename:\n>")
#打开文件
txt = open(filename)
#打印文件内容
print "文件内容为:"
print txt.read()