#!/usr/bin/env python2.7
array_list = [1, 2.3, 3, 4, 5]
ave = 0
for num in array_list:
	ave += float(num) / len(array_list)

print(ave)