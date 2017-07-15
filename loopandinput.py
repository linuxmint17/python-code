#!/usr/bin/env python2.7
import itertools
# 	number=int(raw_input('input integer please'))
# 	if 1<number<100:
# 		break
# 	else:
# 		print 'wrong number ,should be greater than 1 and less than 100 \n'
for i in itertools.count():
	number=int(raw_input('input integer please'))
	if 1<number<100:
		break
	else:
		print 'wrong number ,should be greater than 1 and less than 100\n'

# def to_infinity():
#     index=0
#     while 1:
#         yield index
#         index += 1

# for i in to_infinity():
#     if i > 10:break