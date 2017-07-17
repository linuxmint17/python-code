#!/usr/bin/env python2.7
'transfer Fahrenheit to  Centigrade'
def transferF2C(F):
	c=(F-32)*(5/9.0)
	return c
F=float(raw_input('enter a Fahrenheit number'))
result=transferF2C(F)
print result
