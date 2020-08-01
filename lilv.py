#!/usr/bin/env python3
'calculate  li lv'


def calculi(rate):
    t = 1
    for i in range(1, 366):
        t *= (1 + rate)
    return t


rate = float(input('enter the rate of day\n'))
result = calculi(rate)
print(result)
