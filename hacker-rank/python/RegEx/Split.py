from __future__ import print_function
import re

print(*filter(None, re.split(r'[.,]+', raw_input())), sep='\n')
