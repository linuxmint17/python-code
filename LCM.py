#!/usr/bin/env python2.7
'get  the least common multple'
def lcm(num1,num2):
#	mylist=range(num1,num1*num2+1)
	for i in range(num1,num1*num2+1):
		if i%num1==0 and i%num2==0:
			return i

num1=int(raw_input('enter an integer\n'))
num2=int(raw_input('enter an integer\n'))
if num1<num2:
	num1,num2=num2,num1

result =lcm(num1,num2)
print result