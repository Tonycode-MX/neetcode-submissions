class Solution:
    def isValid(self, s: str) -> bool:
        pile = []
        close_sym = {"(":")","{":"}", "[":"]"}

        for char in s:
            if char == "(" or char == "[" or char == "{":
                pile.append(char)
            else:
                if not pile or char != close_sym[pile[-1]]:
                    return False
                else:
                    pile.pop()

        if not pile:
            return True
        else: return False