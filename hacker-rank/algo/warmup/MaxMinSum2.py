#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))
sumT = reduce(lambda x, y: x+y, arr)

minS = sumT - arr[0]
maxS = sumT - arr[0]

for a in arr[1:]:
    sumTmp = sumT - a
    if minS > (sumTmp):
        minS = sumTmp
    if maxS < (sumTmp):
        maxS = sumTmp

print " ".join(map(str,[minS, maxS]))
    
