#!/usr/bin/env python2.7
'under 1 dollar exchange 25cent 10cent 1cent  the minimum coins  '
def exchangemoney(num):
	num = int(num*100)
	cent25 = num / 25
	cent10 = (num %25) / 10
	cent1 = (num % 25) % 10
	return (cent25, cent10, cent1)


num = float(input('enter a nume greater than 0 and less than 1, only two effective digits\n'))
result = exchangemoney(num)
print('25cent %d 10cent %d 1cent %d' % (result[0], result[1], result[2]))


	