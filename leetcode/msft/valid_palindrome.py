class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j = len(s) -1

        while i<=j:
            print(s[i], s[j])
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            
            if not s[i].isalnum():
                i += 1
            if not s[j].isalnum():
                j -= 1

        return True
    
    def isPalindrome_v2(self, s: str) -> bool:
        """
        extra space to store new string
        """    
        st = [_c.lower() for _c in s if _c.isalnum()]
        st = ''.join(st)
        i = 0
        j = len(st) - 1
        
        while i <= j:
            if st[i].lower() == st[j].lower():
                    i += 1
                    j -= 1
            else:
                return False
        return True 

def main():
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))


if __name__ == '__main__':
    main()


