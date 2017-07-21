#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
import string 
Inputstring=raw_input('string please')
Inputlist=list(Inputstring)
newlist=[]
for i in range(len(Inputlist)):
	if Inputlist[i]!=' ':
		newlist.append(Inputlist[i])
opstr=''
outstring=opstr.join(newlist)
print  outstring
