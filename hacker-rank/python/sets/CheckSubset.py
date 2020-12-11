# More than 4 lines will result in 0 score. Blank lines won't be counted.
for i in range(int(raw_input())):
    a = int(raw_input())
    A = set(raw_input().split())
    b = int(raw_input())
    B = set(raw_input().split())
    print len(A) == len(A & B)
    # A <= B or A.issubset(B)
