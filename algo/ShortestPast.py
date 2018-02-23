#!/bin/python

import sys


def printShortestPath(n, i_start, j_start, i_end, j_end):
    i_tmp, j_tmp = i_start, j_start
    count = 0
    op = []
    if i_tmp % 2 == i_end % 2:
        while i_tmp != i_end:
            if i_tmp > i_end and j_tmp > j_end:
                i_tmp -= 2
                j_tmp -= 1
                op.append('UL')
            elif i_tmp > i_end and j_tmp < j_end:
                i_tmp -= 2
                j_tmp += 1
                op.append('UR')
            elif i_tmp < i_end and j_tmp > j_end:
                i_tmp += 2
                j_tmp -= 1
                op.append('LL')
            elif i_tmp < i_end and j_tmp < j_end:
                i_tmp += 2
                j_tmp += 1
                op.append('LR')
            count += 1
        d = j_end - j_tmp
        ops = 'L' if d < 0 else 'R'
        if abs(d) % 2 == 0:
            for _ in range(abs(d) // 2):
                count += 1
                op.append(ops)
        else:
            print "Impossible"
            return
    else:
        print "Impossible"
        return

    print count
    print " ".join(op)


if __name__ == "__main__":
    # n = int(raw_input().strip())
    # i_start, j_start, i_end, j_end = raw_input().strip().split(' ')
    # i_start, j_start, i_end, j_end = [int(i_start), int(j_start), int(i_end), int(j_end)]
    # printShortestPath(n, i_start, j_start, i_end, j_end)
    printShortestPath(2,0,3,4,3)

