#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-
timestr=raw_input('enter minute')
timenum=int(timestr)
hour=timenum/60
minute=timenum%60
print " %d hours%d minutes" %(hour,minute)