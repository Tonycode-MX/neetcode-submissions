class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [1]*(n+1)
        
        for i in range(n-1, -1, -1):
            res[i] = res[i+1] * nums[i]

        prev_prod = 1
        for i in range(n):
            res[i] = prev_prod * res[i+1]
            prev_prod *= nums[i]

        res.pop()
        return res



