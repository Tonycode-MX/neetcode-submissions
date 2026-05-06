class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, d = 0, len(heights) -1
        max_vol = 0

        while i < d:
            vol = (d-i) * min(heights[i], heights[d])
            if vol > max_vol:
                max_vol = vol

            if heights[i] < heights[d]:
                i+=1
            else:
                d-=1
            
        
        return max_vol
        