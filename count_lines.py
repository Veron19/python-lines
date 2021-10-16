#!/usr/bin/python

marker = 0
f=open ('./text1.txt')
for line in f:
	marker +=1
	print (marker,line)
f.close
