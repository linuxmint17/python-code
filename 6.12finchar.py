#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-
'find char'
def findchr(string,char):
	for i in range(len(string)):
		if   string[i]==char:
			return i
	else:
		return -1
def rfindchr(string,char):
	rstring=string[::-1]
	length=len(string)
	for i in range(length):
		if  rstring[i]==char:
			return length-i-1
	else:
		return -1
def subchr(string,origchar,newchar):
	s=[]
	for i in range(len(string)):
		if string[i]==origchar:
			s.append(newchar)
		else:
			s.append(string[i])
	restr=''.join(s)
	return restr





