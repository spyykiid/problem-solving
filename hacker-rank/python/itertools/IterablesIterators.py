from itertools import combinations
N = int(raw_input())
ip = raw_input().split()
r = int(raw_input())

comb = (list(combinations(ip, r)))
sum = 0
for tupl in comb:
    if 'a' in tupl:
        sum += 1

print float(sum) / len(comb)
