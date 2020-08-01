#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-
import string
inputstr = input('enter a number ')
outputlist=[]
englist=['zero','one','two','three','four',	'five','six','seven','eight','nine']

englsit1=['twenty','thirty','forty','fifty', 'sixty','seventy','eighty','ninety']

englistt2 = ['ten','eleven','twelve','thirteen', 'fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']

englist3 = ['hundred','thousand']

for i in range(len(inputstr)):
	outputlist.append(((englist[string.digits.find(inputstr[i])])))

outstring='-'.join(outputlist) #单词join 拼写错误，debug 了半天，才发现，jion
print(outstring)