#!/usr/bin/env python2.7
'more about sequence'
s='abcde'
for i in [None]+range(-1,-len(s),-1):
	print s[:i]


i = -1
for i in range(-1,-len(s),-1):
	print s[:id]