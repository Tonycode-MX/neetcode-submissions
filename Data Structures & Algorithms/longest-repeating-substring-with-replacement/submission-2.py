class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        n = len(s)
        frec = {}
        for r in range(n):
            frec[s[r]] = frec.get(s[r],0) + 1
            
            while (r-l+1) - max(frec.values()) > k and l<n:
                frec[s[l]] -= 1
                l+=1
            
            res = max(res,r-l + 1)
            


        return res