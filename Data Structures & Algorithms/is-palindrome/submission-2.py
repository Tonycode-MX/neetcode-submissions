class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(c.lower() for c in s if c.isalnum())

        n = len(s) //2

        if s == "":
            return True

        i,j = 0,-1

        for n in range(n):
            if s[i] != s[j]:
                return False
            i+=1
            j-=1

        return True
        