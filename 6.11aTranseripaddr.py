#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
"transfer ip from Dec to bin "
ipsublen = 8
ipstr = input('enter an valid ip addr:\n')
iplist=ipstr.split('.')
biplist=[]
for i in range(len(iplist)):
	subgroup=bin(int(iplist[i]))
	appended=(ipsublen-len(subgroup[2:]))*'0'+subgroup[2:]#sliece and  add some zeros bug already debuged
	biplist.append(appended)
outip=''
outipaddr=outip.join(biplist)
print(outipaddr)


