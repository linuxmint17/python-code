#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-
'this script can get a complex number'
from string import *
symbl = '+-'
realp = []
imagp = []
def atoc(instr):
	rinstr=instr[::-1]
	idx=0
	for i in range(1,len(rinstr)):
		if rinstr[i]!='+' and rinstr!='-':
			imagp.append(rinstr[i])
			idx=i
		else:
			break
	for i in range(idx,len(rinstr)):
		if rinstr[i]!='+' and rinstr!='-':
			realp.append(rinstr[i])
	print(realp)
atoc('+123+234j')
