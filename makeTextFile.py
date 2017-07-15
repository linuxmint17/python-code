#!/usr/bin/env python2.7
'makeTextFile.py --create text file'
import os
ls=os.linesep
#once read aline ended with .
def getfilecontent():
	mylines=[]
	while True:
		entry=raw_input('>: ')
		if entry=='.':
			break
		else:
			mylines.append(entry)
	return mylines
#get filename
while True:
        try:
                fname=raw_input('enter file name')
        except Error,e:
                print "Error:'%s' already exists" %fname ,e
        break
                
	#         fname=raw_input('Enter filename\n')
	# if os.path.exists(fname):
	# 	print "ERROR:'%s' already exists" % fname
	# else:
	# 	break

#use getfilecontent to get each line
mylines=getfilecontent()

#write lines to file
fobj=open(fname,'w')
fobj.writelines(['%s%s'%(x,ls) for x in mylines])
fobj.close()

print 'Done!'
