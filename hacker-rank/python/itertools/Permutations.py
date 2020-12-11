from itertools import permutations

input_str, r = raw_input().split()

for item in sorted(permutations(input_str, int(r))):
    print "".join(item)
