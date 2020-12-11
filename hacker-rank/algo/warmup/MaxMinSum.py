#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))
#sumT = reduce(lambda x, y: x+y, arr)

minVal = sys.maxsize
maxVal = 0
sumT = 0
for a in arr:
    sumT = sumT + a
    if minVal > a:
        minVal = a
    if maxVal < a:
        maxVal = a

print " ".join(map(str,[sumT - maxVal, sumT - minVal]))
