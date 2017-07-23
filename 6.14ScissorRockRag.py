#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-
" a stiupid game"
#　win +even +lose=9 condition
import random
Scissors=('S','s','Scirror','scissor')
Rocks=('R','r','Rock','Rock')
Rags=('g','G','Rag','rag')
tools=('Scissor','Rock','Rag')
AIchocie=random.randint(0,2)
AI=tools[AIchocie]
PPchoice=raw_input("enter your choice :\
		\n(S)cirror \n(R)ock\nRa(g)\n")
choice=0
if PPchoice in Scissors:
	choice=0
elif PPchoice in Rocks:
	choice=1
elif PPchoice in Rags:
	choice=2
else:
	print 'wrong choice '
result=AIchocie-choice
if result==0:
	print 'even',AI 
elif result in [-2,1]:
	print 'AIwin',AI
else:
	print "you Win",AI
