#!/usr/bin/env python2.7
'judge a student  achievement'
def judgescore(num):
	if 90<=num<=100:
		return 'A'
	elif 80<=num<=89:
		return 'B'
	elif 70<=num<=79:
		return 'C'
	elif 60<=num<=69:
		return 'D' 
	elif 0<=num<=60:
		return 'F'
	else :
		return 'None'

num=int(raw_input('enter the score '))

# ss=judgescore(num)
# print ss