#!/usr/bin/env  python2.7
dict1={'hello':123,'jack':23,'bob':56,'suse':45}
li=dict1.keys()
li.sort()
print li
for key in li:
    print " %s : %s"%(key,dict1[key]),



