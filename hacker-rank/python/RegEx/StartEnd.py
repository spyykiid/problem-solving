import re
S = raw_input()
k = raw_input()
anymatch = 'No'
for m in re.finditer(r'(?=(' + k + '))', S):
    anymatch = 'Yes'
    print (m.start(1), m.end(1) - 1)
if anymatch == 'No':
    print (-1, -1)

''' Solution from Discussion '''
# import re
# s = input()
# k = input()
#
# matches = list(re.finditer(r'(?={})'.format(k), s))
#
# if matches:
#     print('\n'.join(str((match.start(),
#           match.start() + len(k) - 1)) for match in matches))
# else:
#     print('(-1, -1)')
