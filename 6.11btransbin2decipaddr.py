#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
ipstr=raw_input('enter bin ip addr plz\n')
if len(ipstr)!=32:
	print "wrong ip add ,please check\n"
s=[ipstr[0:8],ipstr[8:16],ipstr[16:24],ipstr[24:32]]

outip=[]
for i in range(len(s)-1):
	outip.append(repr(int(s[i],2))+'.')

outip.append(int(s[3],2))

print outip