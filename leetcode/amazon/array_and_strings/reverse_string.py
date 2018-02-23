def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    # if len(s) <= 1:
    #     return s
    # else:
    #     return self.reverseString(s[1:]) + s[0]

    # slen = len(s)
    # result = ""
    # while slen > 0:
    #     result += s[slen-1]
    #     slen -= 1
    # return result

    '''One line python way to reverse'''
    return s[::-1]


print(reverseString('a palm'))