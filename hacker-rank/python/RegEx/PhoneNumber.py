import re

for _ in range(int(raw_input())):
    print 'YES' if bool(re.match(r'[789]\d{9}$', raw_input())) else 'NO'
