#!/bin/python
from __future__ import print_function
from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


[print(*c) for c in OrderedCounter(sorted(raw_input())).most_common(3)]
