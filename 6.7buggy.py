#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
#输入一个字符串形式的数字
num_str = input('enter a number :')
#转成整数
num_num = int(num_str)
#因子列表从1到num_num
fac_list = range(1, num_num+1)

print("BEFORE:", fac_list)
#输出之前的因子列表
i = 0
#去掉整除数字的因子
while i < len(fac_list):

	if num_num % fac_list[i] == 0:
		del fac_list[i]

	i = i + 1
#输出结果
print("AFTER:", fac_list)
