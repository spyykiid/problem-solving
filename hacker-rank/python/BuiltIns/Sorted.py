#!/bin/python
from __future__ import print_function
import sys

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = []
    for arr_i in xrange(n):
        arr_temp = map(int, raw_input().strip().split(' '))
        arr.append(arr_temp)
    k = int(raw_input().strip())
    arr_sorted = sorted(arr, key=lambda x: x[k])

    for items in arr_sorted:
        print(*items, end="\n")
