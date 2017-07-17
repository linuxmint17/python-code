#!/usr/bin/env python2.7
'classic problem of leap year'
def judgeleap(num):
	if num%4!=0:
		return 'non leap year'
	elif num%100!=0 :
		return 'leap year'
	elif num%400!=0:
		return 'non leap year'
	else:
		return 'leap year'
year=int(raw_input('enter a year'))
result=judgeleap(year)
print '%s is %s' %(year,result)