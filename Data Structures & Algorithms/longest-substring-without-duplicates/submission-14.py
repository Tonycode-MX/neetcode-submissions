class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        n = len(s)
        l = 0
        substr = set()

        for r in range(n):
            if s[r] in substr:
                while s[r] in substr:
                    substr.remove(s[l])
                    l+=1
                substr.add(s[r])
            else:
                substr.add(s[r])

            res = max(res,r-l+1)

        return res