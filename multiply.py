#!/usr/bin/env python2.7
'receive two number return their multiply result'
def multiply(num1,num2):
	result=(num1)*(num2)
	if result.imag==0:
		print result.real
		return result.real
	else:
		print result
		return result
	
	

num1=complex(raw_input('enter num1\n'))
num2=complex(raw_input('enter num2\n'))

multiply(num1,num2)