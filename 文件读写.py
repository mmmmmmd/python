# -*- coding:utf-8 -*-

filename = raw_input("Please input the filename:\n>")

print "We're going to erase %r" %filename
print "If you don't want that,hit CTRL-C(^C)."
print "If you want  that,hit RETURN."

print "open the file..."
target = open(filename,'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
