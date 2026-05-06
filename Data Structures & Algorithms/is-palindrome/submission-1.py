class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s) //2

        s = "".join(c.lower() for c in s if c.isalnum())

        if s == "":
            return True

        i,j = 0,-1

        for n in range(n):
            if s[i] != s[j]:
                return False
            i+=1
            j-=1

        return True
        