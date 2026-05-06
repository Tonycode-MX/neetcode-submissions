class Solution:
    def isPalindrome(self, s: str) -> bool:

        i,d = 0,len(s) - 1

        while i < d:
            if not s[i].isalnum():
                i+=1
            elif not s[d].isalnum():
                d-=1
            elif s[i].lower() != s[d].lower():
                return False
            else:
                i+=1
                d-=1
        return True
        