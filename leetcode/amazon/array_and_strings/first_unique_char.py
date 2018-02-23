def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    sdict = {}
    for i, x in enumerate(s):
        if sdict.get(x):
            count, index = sdict[x]
            sdict[x] = (count + 1, index)
        else:
            sdict[x] = (1, i)

    res = len(s)
    for k, v in sdict.items():
        count, idx = v
        if count == 1 and idx < res:
            res = idx

    if res == len(s):
        return -1
    else:
        return res