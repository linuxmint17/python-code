#!/usr/bin/env python2.7
person=['name',['saving',100.00]]
hubby=person[:] # slice copy
wifey=list(person) #fac func copy
print hubby,wifey
print [id(x) for x in person,hubby,wifey]
print id(person[1][1]),id(hubby[1][1]),id(wifey[1][1])
hubby[1][1]=50.00
print hubby,wifey

