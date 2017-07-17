#!/usr/bin/env python2.7
'calculate  li lv'
def calculi(rate):
	t=1
	for i in range(1,366):
		 t*=(1+rate)
	return t
rate=float(raw_input('enter the rate of day'))
result=calculi(rate)
print result