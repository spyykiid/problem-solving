
'''
Given an integer list M and an integer target T, write a function that finds three unique integers
a, b, c within M where a + b + c = T return all sets of a, b, c found.

example:
M = [8, 3, 7, 4, 0, -2, 6, 1], T = 9

output:
[[8, -2, 3],
 [3, 0, 6]]

also
correct:
[[-2, 3, 8],
 [6, 3, 0]]   '''


def threeSum(M, T):
    result = []
    for a, i in enumerate(M):
        new_target = T - a
        map_ = {}
        for b, j in enumerate(M):
            if b == a and i == j:
                continue
            c = new_target - b
            if c in map_:
                result.append([a, map.get(c), b])
        map_[b] = b

    return result



