class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searcher(left, right):
            if left > right:
                return -1
            
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                return searcher(mid+1, right)
            
            elif nums[mid] > target:
                return searcher(left, mid-1)
        
        return searcher(0, len(nums)-1)
            







        