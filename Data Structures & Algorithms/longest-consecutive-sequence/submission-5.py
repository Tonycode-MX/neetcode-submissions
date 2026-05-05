class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        res = 1

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                count = 1
                while current_num + 1 in num_set:
                    count+=1
                    current_num+=1
                if count > res:
                    res = count
        return res

        