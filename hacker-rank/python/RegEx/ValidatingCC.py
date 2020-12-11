
import re

for _ in range(int(raw_input())):
    cc = raw_input().strip()
    if bool(re.search(r'^[456]\d{15}$', cc)) or bool(re.search(r'^([4-6]\d{3})(-\d{4}){3}$', cc)):
        if bool(re.search(r'([0-9])(-?\1){3}', cc)):
            print 'Invalid'
        else:
            print 'Valid'
    else:
        print 'Invalid'

'''Problem setters solution'''
# Part1 :
# Check if credit card number size if exactly 16, all the characters are integers and - symbol may be present after every group of 4 digits
# All the above checks can be validated using : r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$'

# Part2:
# Check is credit card number has 4 or more repeating consecutive digits
# This check can be validated using : r'(\d)\1{3,}''

# import re
# for i in range(int(raw_input())):
#     S = raw_input().strip()
#     pre_match = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$', S)
#     if pre_match:
#         processed_string = "".join(pre_match.group(0).split('-'))
#         final_match = re.search(r'(\d)\1{3,}', processed_string)
#         print 'Invalid' if final_match else 'Valid'
#     else:
#         print 'Invalid'
