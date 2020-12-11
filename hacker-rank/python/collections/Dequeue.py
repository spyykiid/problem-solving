from __future__ import print_function
from collections import deque

d = deque()

for _ in range(int(raw_input())):
    lst = raw_input().split()
    if lst[0] == 'append':
        d.append(lst[1])
    elif lst[0] == 'appendleft':
        d.appendleft(lst[1])
    elif lst[0] == 'pop':
        d.pop()
    else:
        d.popleft()

print(*d, end=' ')
