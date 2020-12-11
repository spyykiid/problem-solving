import re
for _ in range(int(raw_input())):
    try:
        regex = re.compile(raw_input())
        print True
    except re.error:
        print False
