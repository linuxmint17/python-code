#!/usr/bin/env python2.7
'under 1 dollar exchange 25cent 10cent 1cent  the minimum coins  '
def exchangemoney(num):
	num=int(num*100)
	cent25=num/25
	cent10=(num%25)/10
	cent1=(num%25)%10
	return (cent25,cent10,cent1)


num=float(raw_input('enter a numer greater than 0\nand less than 1,\nonly two effictive digits\n'))
result=exchangemoney(num)
print '25cent %d 10cent %d 1cent %d' % (result[0],result[1],result[2])


	