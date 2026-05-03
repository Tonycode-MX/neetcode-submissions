class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1
        contain_zero = 0
        for n in nums:
            if n != 0:
                product *= n
            else:
                contain_zero += 1
        
        res = []
        if contain_zero > 1 :
            return [0]*len(nums)
        elif contain_zero == 1:
            for n in nums:
                if n == 0:
                    res.append(product)
                else:
                    res.append(0)
        else:
            for n in nums:
                res.append((product//n))
        return res
                


            
        

        
        