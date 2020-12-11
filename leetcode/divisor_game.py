class Solution:
    def divisorGame(self, N: int) -> bool:
        return N%2 == 0

def main():
    s = Solution()
    print(s.divisorGame(5))

if __name__ == '__main__':
  main()