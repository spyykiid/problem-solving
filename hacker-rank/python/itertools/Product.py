from itertools import product

A = map(int, raw_input().split())
B = map(int, raw_input().split())

for x, y in list(product(A, B)):
    print (x, y),

# for item in product(A,B):
#   print item,

# Sol in Python 3
# for item in product(A, B):
#    print(item, end=' ')
