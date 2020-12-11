from itertools import combinations_with_replacement
ip_str, r = raw_input().split()

for item in list(combinations_with_replacement(sorted(ip_str), int(r))):
    print ''.join(item)
