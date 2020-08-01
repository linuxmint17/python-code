#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
Inputstring = input('string please')
Inputlist = list(Inputstring)
newlist = []
for i in range(len(Inputlist)):
	if Inputlist[i] != ' ':
		newlist.append(Inputlist[i])
outputstr = ''
outstring = outputstr.join(newlist)
print(outstring)
