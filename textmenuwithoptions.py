#!/usr/bin/env python2.7
#def sumfivenumber(mylist[]=[0,0,0,0,0]):
options=('(1)get sum five numbers',\
	'(2)get average of five numbers','(X)exit')
mylist=[0,1,2,3,4]

def showmenu():
	for opt in options:
		print opt

def inputalist():
	for i in range(5):
		mylist[i]=float(raw_input('enter a number '))
	return mylist

def sumfive():
	mysum=0
	for i in range(5):
		mysum+=mylist[i]
	return mysum


def avefive():
	myave=0
	for i in range(5):
		myave+=mylist[i]/5.0
	return myave
condition=True
mylist=inputalist()
while condition:
	
	#print mylist

	showmenu()
	flag=raw_input('select function wiht 1 or2 or X\n')
	if flag=='1':
		s=sumfive()
		print s
	elif flag=='2':
		print avefive()
	elif flag=='X'or flag=='x':
		condition=False
	





