#!/usr/bin/env python2.7
'generate 100 random number to make up a list'
import random
mylist=[]
for i in range(100):
	t=random.randint(0,2**23-1)
	mylist.append(t)
mylist.sort()

print mylist