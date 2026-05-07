class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for num in range(n-2):
            if num > 0 and nums[num] == nums[num-1]:
                continue
            i,d = num+1,n-1    
            while i<d:
                if nums[i] + nums[d] == (-1)*nums[num]:
                    res.append([nums[num], nums[i], nums[d]])
                    i+=1
                    d-=1
                    while i < d and nums[d] == nums[d+1]:
                        d-=1
                    while i < d and nums[i] == nums[i-1]:
                        i+=1
                elif nums[i] + nums[d] > (-1)*nums[num]:
                    d-=1
                else:
                    i+=1
        return res


