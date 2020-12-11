from math import floor, log2

class Solution:
    def bitwiseComplement(self, N: int) -> int:
      if N == 0:
          return 1
      todo, bit = N, 1
      while todo:
        print(todo, N, bit)
        # flip current bit
        N = N ^ bit
        # prepare for the next run
        bit = bit << 1
        todo = todo >> 1
      return N

    def bitwiseComplement_v2(self, N: int) -> int:
        if N == 0:
            return 1
        # l is a length of N in binary representation
        l = floor(log2(N)) + 1        
        # bitmask has the same length as N and contains only ones 1...1
        bitmask = (1 << l) - 1
        print(l, bitmask)
        # flip all bits
        return bitmask ^ N

s= Solution()

print(s.bitwiseComplement(5))

print(s.bitwiseComplement_v2(5))