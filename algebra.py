#!/usr/bin/env python2.7
def algebra(inputstr):
	mylist=inputstr.split()
	num1=float(mylist[0])
	num2=float(mylist[2])
	if mylist[1]=='+':
		return num1+num2
	if mylist[1]=='-':
		return num1-num2
	if mylist[1]=='*':
		return num1*num2
	if mylist[1]=='/':
		return num1/num2
	if mylist[1]=='**':
		return num1**num2
	if mylist[1]=='%':
		return num1%num2

inputstr = input("enter a experssion like ' 1 + 2'\nseparate number and the operator with blank\n")
result=algebra(inputstr)
print(result)