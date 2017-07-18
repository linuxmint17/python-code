#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
'use list to manipulate stack'
stack=[]
def pushit():
	stack.append(raw_input('Enter New string: ').strip())

	def popit():
		if len(stack)==0:
			print 'cant not pop from an empty stack'
		else:
			print'removed [', 'stack.pop()',']'
	def viewstack():
		print stack 

	CMDs={'u':putshi,'o':popit,'v':viewstack}
	def showmenu():
		pr="""
		p(U)sh
		p(O)p
		(v)iew
		(Q)uit

		Enter choice:"""

while True:
	while True:
		try:
			choice=raw_input(pr).strip()[0].lower()
        except (EOFError,KeyboardInterrupt,IndexError):

            choice='q'

	 			print '\n You picked:[%s]' %choice
	 			if choice not in 'uovq':
	 				print 'Invalid option,try again'
	 			else:
	 				break
	 	if choice=='q':
	 		break
	 		CMDs[choice]()

	 	if __name__=='__main__':
	 		showmenu()
