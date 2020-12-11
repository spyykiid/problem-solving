from itertools import combinations
ip_str, r = raw_input().split()
for i in range(1, int(r) + 1):
    for item in list(combinations(sorted(ip_str), i)):
        print ''.join(item)
