#!/usr/bin/env python2.7
'without function isinstance() ,to make a typecheck'
'version1'
def displayNumType(num):
	print num, "is",
	if type(num)==type(0):
		print 'an integer'
	elif type(num)==type(0L):
		print 'a long'
	elif type(num)==type(0.0):
		print 'a float'
	elif type(num)==type(0+0j):
		print 'a complex number'
	else:
		print 'not a number'

displayNumType(69)
displayNumType(9999999999999999999)
displayNumType(12.3)
displayNumType(2+3j)
displayNumType('xxx')
