#!/usr/bin/env python2.7
'without function isinstance() ,to make a typecheck'
'version 2'
import types
def displayNumType(num):
	print num, "is",
	if type(num)==types.IntType:
		print 'an integer'
	elif type(num)==types.LongType:
		print 'a long'
	elif type(num)==types.FloatType:
		print 'a float'
	elif type(num)==types.ComplexType:
		print 'a complex number'
	else:
		print 'not a number'
		
displayNumType(69)
displayNumType(9999999999999999999)
displayNumType(12.3)
displayNumType(2+3j)
displayNumType('xxx')