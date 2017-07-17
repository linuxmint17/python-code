#!/usr/bin/env python2.7
'payment balance'
def payment(opbal,monpay):
	pymt=0
	print 'pymt    Paid    balance'
	print '-----	---    -------'
	while opbal-monpay>0:
		pymt+=1
		print '%d    $%-.2f   $%-.2f'%(pymt,monpay,opbal-monpay)
		opbal-=monpay

	print '%d    $%.2f    $0.00'%(pymt+1,opbal)

opbal=float(raw_input('enter the opbal\n'))
monpay=float(raw_input('enter the monpay\n'))

payment(opbal,monpay)
