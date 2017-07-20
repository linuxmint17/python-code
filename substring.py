#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-
"substring(str1,substr), if substr exist ,return True"
import string
def substring(str1,substr):
	if str1.count(substr)!=0:
		return True
	else:
		return False

print substring('jackshepehrd888susesue','su')