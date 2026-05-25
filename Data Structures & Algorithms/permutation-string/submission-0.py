class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        windowLen = len(s1)
        
        s1_letters = [0]*26
        for letter in s1:
            index = ord(letter) - ord("a")
            s1_letters[index] += 1

        window_letters = [0]*26
        for letter in s2[:windowLen-1]:
            index = ord(letter) - ord("a")
            window_letters[index] += 1

        for window in range(len(s2)-windowLen+1):
            newLetter = ord(s2[window+windowLen-1]) - ord("a")
            window_letters[newLetter] += 1

            if window_letters == s1_letters:
                return True

            first_letter = ord(s2[window]) - ord("a")
            window_letters[first_letter] -= 1

        return False


        # [1,2,3,4,5,6,7,8,9,0]
        # 2
        