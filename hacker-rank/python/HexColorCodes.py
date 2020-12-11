import re
str_ = "\n".join([raw_input() for _ in range(int(raw_input()))])

# lst_ = re.findall(r'#([a-f0-9]{3,6})(?!\n)',str_,re.I)
lst_ = re.findall(r'(#(?:[\da-f]{3}){1,2})(?!\s)', str_, re.I)

print '\n'.join(lst_)
