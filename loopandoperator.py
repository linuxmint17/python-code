#!/usr/bin/env python2.7
# s=0.0
# mylist=[1,2,3,4,5]
# # for i in range(5):
# # 	s+=mylist[i];
# # print s
# i=0
# while i<5:
# 	s+=mylist[i]
# 	i+=1

# print s
mylist=[0,0,0,0,0]
s=0
i=0
# while i in range(5):
# 	mylist[i]=float(raw_input('input integers'))
# 	s+=mylist[i]
# 	i+=1

for i in range(5):
	mylist[i]=float(raw_input('input integers'))
	s+=mylist[i]

print s