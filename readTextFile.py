#!/usr/bin/env python2.7
'readTextFile.py -- read and display text'
import os

fname=raw_input('enter filename:')
print 

#attempt to open file for reading
if  not os.path.exists(fname):
	print "Error :'%s' does not s exists " % fname
else:
	fobj=open(fname,'r')
	for eachLine in fobj:
		print eachLine,
	fobj.close()
# try:
# 	fobj=open(fname,'r')
# except IOError,e:
# 	print "*** file open error",e
# else:
# 	#display contents to screen
# 	for eachLine in fobj:
# 		print eachLine,
# 	fobj.close()