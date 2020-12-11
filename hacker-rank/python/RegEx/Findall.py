import re

list_ = map(lambda x: x.group(), re.finditer(
    r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]){2,}(?=[qwrtypsdfghjklzxcvbnm])', raw_input(), re.IGNORECASE))
if list_:
    print '\n'.join(list_)
else:
    print -1

'''Another solution'''
# import re
# v = "aeiou"
# c = "qwrtypsdfghjklzxcvbnm"
# m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
# print('\n'.join(m or ['-1']))

''' Problem setter code'''
# import re
# consonants = 'qwrtypsdfghjklzxcvbnm'
# vowels = 'aeiou'
# match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',raw_input(),flags = re.I)
# if match:
#     for i in match:
#         print i
# else:
#     print -1
