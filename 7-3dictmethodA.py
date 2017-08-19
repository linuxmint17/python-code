#!/usr/bin/env  python2.7
# -*- coding:utf-8 -*-
dict1={'tiaottiaohu':1234,'hello':123,'jack':23,'bob':56,'suse':45}
li=dict1.keys()
li.sort()
# for key in li:
#     print " %s : %s"%(key,dict1[key]),

dict2=dict1
li2=sorted(dict2.iteritems(),key=lambda t:t[1],reverse=True)
print li2

