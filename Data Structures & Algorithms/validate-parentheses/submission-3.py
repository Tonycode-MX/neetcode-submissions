class Solution:
    def isValid(self, s: str) -> bool:
        pile = []
        close_sym = {"(":")","{":"}", "[":"]"}

        for char in s:
            if char in close_sym:
                pile.append(char)
            else:
                if not pile or char != close_sym[pile[-1]]:
                    return False
                pile.pop()

        return len(pile) == 0
        
        
        