from __future__ import print_function
from collections import OrderedDict

ordered_dict = OrderedDict()
for _ in range(int(raw_input())):
    key = raw_input()
    ordered_dict[key] = ordered_dict.get(key, 0) + 1

print(len(ordered_dict))
for count in ordered_dict.values():
    print(count, end=" ")
