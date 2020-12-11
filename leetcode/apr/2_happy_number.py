"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
def get_squares(N):
  result = 0
  while N>0:
    last = N%10
    result += last*last
    N = N//10
    print(N, result, last)
  return result

def isHappy(n: int) -> bool:
  # x = n
  # while True:
  #   squared = get_squares(x)
  #   if squared == 1:
  #     return True
  #   else:
  #     x = squared
  seen= set()
  while n!=1 and n not in seen:
    seen.add(n)
    n = self.get_squares(n)
  return n == 1
  

def main():
  # print(get_squares(10))
  print(isHappy(19))
if __name__ == "__main__":
    main()