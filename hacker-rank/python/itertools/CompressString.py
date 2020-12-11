from itertools import groupby
ip = raw_input()
for k, g in groupby(ip):
    print (len(list(g)), int(k)),
