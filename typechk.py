#!/usr/bin/env python2.7
'typechk.py to check the type of obj'

def displayNumType(num):
	print num , 'is ',
	if isinstance(num,(int ,long,float,complex)):
		print 'a number of type:',type(num).__name__
	else:
		print 'not a number'

displayNumType(-69)
displayNumType(9999999999999999999999)
displayNumType(98.4)
displayNumType(-5.2+1.4j)
displayNumType('xxxxxasdfsdasdfsadfsadfsdaf')