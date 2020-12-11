#!/bin/python

import sys

def solve(a_triplet, b_triplet):
    A = 0
    B = 0
    for a_val, b_val in zip(a_triplet, b_triplet):
        if a_val > b_val:
            A += 1
        elif a_val < b_val:
            B += 1 
   
    return [A,B]           

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve([a0, a1, a2],[ b0, b1, b2])
print " ".join(map(str, result))
