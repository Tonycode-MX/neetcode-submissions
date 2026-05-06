class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, d = 0, len(heights) -1
        max_vol = (d-i) * min(heights[i], heights[d])

        while i < d:
            if heights[i] < heights[d]:
                i+=1
            elif heights[d] < heights[i]:
                d-=1
            else:
                if heights[d-1] > heights[d]:
                    d-=1
                else:
                    i+=1
            vol = (d-i) * min(heights[i], heights[d])
            if vol > max_vol:
                max_vol = vol
        
        return max_vol
        