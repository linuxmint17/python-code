#!/usr/bin/env python2.7
'qu yu exercises'
# for i in range(21):
# 	if i%2==0:
# 		print i,
# for i in range(21):
# 	if i%2!=0:
# 		print i,
num1=int(raw_input('enter an integer\n'))
num2=int(raw_input('enter an integer\n'))
if num1<num2:
	num1,num2=num2,num1

if num1%num2==0:
	print True
else:
	print False