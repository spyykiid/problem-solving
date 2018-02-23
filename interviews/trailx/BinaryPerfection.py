import math
import sys


def generate_answer():
    height = int(sys.stdin.readline().strip())
    p = [int(num) for num in sys.stdin.readline().strip().split()]

    ans = []
    for x in p:
        if (True):
            currentHeight = height
            node = int(math.pow(2, height) - 1)
            if x == node:
                ans.append(-1)
            else:
                nodeBE = int(math.pow(2, currentHeight) - 2)
                nodeL = int(node - int(nodeBE / 2) - 1)
                nodeR = int(node - 1)
                h = 0
                while (x != nodeR and x != nodeL and h < 30):
                    h += 1
                    if (x > nodeL):
                        node = nodeR
                    else:
                        node = nodeL
                    currentHeight = currentHeight - 1
                    nodeBE = int(math.pow(2, currentHeight) - 2)
                    nodeL = node - (nodeBE / 2) - 1
                    nodeR = node - 1
                ans.append(node)

                #   q = [1, 2, 3]
    print(" ".join([str(num) for num in ans]))

