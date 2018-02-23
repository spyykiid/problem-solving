import itertools




def findAnagrams(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    p_ana = ["".join(perm) for perm in itertools.permutations("p")]
    p_len = len(p)
    for i, s_ in enumerate(s):
        if i in s_:
            pass



