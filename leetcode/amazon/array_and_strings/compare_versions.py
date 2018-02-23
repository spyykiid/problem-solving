def compareVersion(self, version1, version2):
    v1 = version1.split('.')
    v2 = version2.split('.')
    v1l = len(v1)
    v2l = len(v2)

    if v1l < v2l:
        v1 += ['0'] * (v2l - v1l)
    elif v1 > v2:
        v2 += ['0'] * (v1l - v2l)
    v1 = map(int, v1)
    v2 = map(int, v2)
    res = 0
    for i, j in zip(v1, v2):
        if i == j:
            continue
        elif i < j:
            res = -1
            break
        else:
            res = 1
            break
    return res