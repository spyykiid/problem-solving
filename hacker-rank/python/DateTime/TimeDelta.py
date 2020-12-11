#!/bin/python3

from datetime import datetime
for _ in range(int(raw_input())):
    t1 = datetime.strptime(raw_input(), '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(raw_input(), '%a %d %b %Y %H:%M:%S %z')
    print (int(abs((t1 - t2).total_seconds())))
