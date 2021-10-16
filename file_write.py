#!/usr/bin/python

with open("test.txt", "+a") as file:
    file.write("hello world\n")

    file.close
f=open("test.txt")
t= f.read()
print ('123\n'+t)
f.close
