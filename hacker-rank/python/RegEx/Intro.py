import re

for _ in range(int(raw_input())):
    print bool(re.match(r"(-|\+)?[0-9]*\.[0-9]+$", raw_input()))
