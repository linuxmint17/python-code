#!/usr/bin/env python2.7
'this script use to known the artuibute of an obj'
import os
ls=os.linesep
exists=os.path.exists
condition=True
while condition:
	fname=raw_input('Enter item you would like to know\n Enter x to exists this program \n Check the attribute in file\n')
	if fname=='x' or fname=='X':
		condition=False
	if exists(fname):
		print '%s already exist' % fname
		print 'cover it or not (yes/no)'
		flag=raw_input();
		if flag=='no' or flag=='n':
			break

	fobj=open(fname,'w')
	fobj.writelines(['%s%s'%(t,ls) for t in dir(fname)])	
	fobj.close()





