n = raw_input()
s = set(map(int, raw_input().split()))

for _ in range(int(raw_input())):
    op = raw_input()
    try:
        if op == 'pop':
            s.pop()
        else:
            operation, num = op.split(' ')
            if operation == 'remove':
                s.remove(int(num))
            elif operation == 'discard':
                s.discard(int(num))
    except KeyError:
        continue

print str(sum(s))
