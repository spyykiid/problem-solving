from __future__ import print_function
from collections import OrderedDict

ordered_dict = OrderedDict()

for _ in range(int(raw_input())):
    key, count = raw_input().rsplit(' ', 1)
    ordered_dict[key] = ordered_dict.get(key, 0) + int(count)

for key, countk in ordered_dict.items():
    print(key, countk, end="\n")
