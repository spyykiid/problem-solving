#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    maxV = 0
    maxC = 0
    for a in ar:
        if a > maxV:
            maxV = a
            maxC = 1
        elif a == maxV:
            maxC += 1    
    return maxC        

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)


