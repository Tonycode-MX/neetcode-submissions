class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = set()
        for char in nums:
            if char in uniques:
                return True
            uniques.add(char)
        return False

        