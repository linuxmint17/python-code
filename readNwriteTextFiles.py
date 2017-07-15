#!/usr/bin/env python2.7
#-*- coding:utf8 -*-
"readNwriteTextFiles --just as the name says"
import os
ls=os.linesep
menu=('1>create a file ','2>show a file content','x>exit')
#get file namefunciton
def getfilename():
	while True:
		fname=raw_input('enter a file name \n')
		if os.path.exists(fname):
			print "Error '%s' already exists" % fname
		else:
			break
	return fname

#display the selection menu
def displaymenu():
	for item in menu:
		print item
#output eachline
def readtextfun():
	fname=raw_input('enter filename:')
	print 
	if not os.path.exists(fname):
		print "Error ’%s' does not exit" % (fname)
	else:
		fobj=open(fname,'r')
		for eachLine in fobj:
			print eachLine.strip()
		fobj.close()
#define this function to easier the  createfilefun
def getfilecontent():
	mylines=[]
	while True:
		entry=raw_input('>: ')
		if entry=='.':
			break
		else:
			mylines.append(entry)
	return mylines
#create a file
def createfilefun():
	fname=getfilename()
	mylines=getfilecontent()
	fobj=open(fname,'w')
	fobj.writelines(['%s%s'%(x,ls) for x in mylines])    #write lines to file
	fobj.close()

condition=True
while condition:
	displaymenu()
	flag=raw_input('enter you choice \n')
	if flag=='1':
		createfilefun()
	elif flag=='2':
		readtextfun()
	elif flag=='x' or flag=='X':
		condition=False