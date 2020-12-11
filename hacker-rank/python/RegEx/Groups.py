from __future__ import print_function
import re

mobj = re.search(r'([a-zA-Z0-9])\1+', raw_input())
print(mobj.group(1)) if mobj else print(-1)
