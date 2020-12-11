class Solution:
  def majorityElement(self, nums):
    major = len(nums) // 2
    c = {}
    for n in nums:
      val = c.get(n, 0) + 1
      c[n] = val
      if val > major:
        return n
  
    def majorityElementv2(self, nums):
      count = 0
      candidate = None

      for num in nums:
          if count == 0:
              candidate = num
          count += (1 if num == candidate else -1)

      return candidate 





def main():
  s = Solution()
  test_case = [3,2,3]
  print(s.majorityElement(test_case))


if __name__ == '__main__':
  main()