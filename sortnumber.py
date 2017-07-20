#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-
"sort numbers in alphabet  or real big small"
# real big small
# mynumber=raw_input('enter a string number seperate by blank \n')
# listnumber=list(mynumber.split())
# listnumber.sort()
# print str(listnumber)
# in alphabet
mynumber=raw_input('enter a string number seperate by blank \n')
listnumber=list(mynumber.split())
# bubble sort
length=len(listnumber)
for i in range(length):
	for j in range(length-1):
		if listnumber[j]>listnumber[j+1]:
			listnumber[j],listnumber[j+1]=\
			listnumber[j+1],listnumber[j]

print listnumber