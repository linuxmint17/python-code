#!/usr/bin/env python2.7
a=raw_input('enter a number ')
b=raw_input('enter a number ')
c=raw_input('enter a number ')

def mymax(a,b):
	if a>b:
		maxnum=a
	else:
		maxnum=b
	return maxnum
def mymin(a,b):
	if a<b:
		minnum=a
	else:
		minnum=b
	return minnum
maxnum=mymax(mymax(a,b),c)
minnum=mymin(mymin(a,b),c)
def mymid(a,b,c):
	if a!=maxnum and a!=minnum:
		mymid=a
	elif b!=maxnum and b!=minnum:
		mymid=b
	else:
		mymid=c
	return mymid 
midnum=mymid(a,b,c)
print maxnum ,midnum,minnum