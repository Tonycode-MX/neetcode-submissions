class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_map = {}
        for n in nums:
            right_map[n] = right_map.get(n,0)+1
        
        left_map = {}
        res = []
        for mid_val in nums:
            right_map[mid_val] -= 1

            right_prod = 1
            for element in right_map:
                right_prod *= (element**right_map[element])

            left_prod = 1
            for element in left_map:
                left_prod *= (element**left_map[element])

            res.append((right_prod * left_prod))

            left_map[mid_val] = left_map.get(mid_val,0) + 1
        
        return res
        