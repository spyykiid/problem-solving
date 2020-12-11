A = set(map(int, raw_input().split()))

for _ in range(int(raw_input())):
    s = set(map(int, raw_input().split()))
    if s <= A and len(A - s) > 0:
        continue
    else:
        print "False"
        exit()
print "True"

# Solution 2
# A = set(raw_input().split())
# print all(map(lambda x: (A > x), [set(raw_input().split()) for i in range(int(raw_input()))]))
