from pythonds.basic.stack import Stack

def reverseString(str):
    if len(str) == 1:
        return str[0]
    else:
         return reverseString(str[1:]) + str[0]

print(reverseString('Rahul'))