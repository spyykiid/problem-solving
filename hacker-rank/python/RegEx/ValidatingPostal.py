import re
postl = raw_input().strip()

print bool(re.search(r'^[1-9]\d{5}$', postl)) and bool(len(re.findall(r'(?=(\d)\d\1)', postl)) <= 1)
