class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product_arr = [1]*(len(nums)+1)
        i = len(nums)-1

        while i > -1:
            product_arr[i] = product_arr[i+1] * nums[i]
            i-=1

        res = []
        prev_prod = 1
        for i in range(len(nums)):
            res.append(prev_prod * product_arr[i+1])
            prev_prod *= nums[i]

        return res