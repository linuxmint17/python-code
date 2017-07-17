#!/usr/bin/env python2.7
'get greatest common divisor'
def gcd(num1,num2):
	if num2==0:
		return 0
	while num1%num2:
		num1,num2=num2,num1%num2
	return num2
num1=int(raw_input('enter an integer\n'))
num2=int(raw_input('enter an integer\n'))
if num1<num2:
	num1,num2=num2,num1
result=gcd(num1,num2)
print result