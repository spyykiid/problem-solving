from collections import Counter
class Solution:
  def firstUniqChar(self, s: str) -> int:
    
    c = Counter(s)

    for i, _s in enumerate(s):
      if _s in c and c[_s] == 1:
         return i
    return -1 

def main():
  s = Solution()
  resp = s.firstUniqChar('leetcode')
  print(resp)

if __name__ == '__main__':
  main()