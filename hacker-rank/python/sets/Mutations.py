N = raw_input()
A = set(raw_input().split())

for _ in range(int(raw_input())):
    op, n = raw_input().split()
    x = set(raw_input().split())
    if op == 'intersection_update':
        A &= x
    elif op == 'update':
        A |= x
    elif op == 'symmetric_difference_update':
        A ^= x
    else:
        A -= x

print sum(map(int, A))
