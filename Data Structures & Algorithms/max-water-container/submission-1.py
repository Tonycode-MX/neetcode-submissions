class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i, d = 0, len(heights) -1
        max_vol = (d-i) * min([heights[i], heights[d]])

        while i < d:
            while heights[i] < heights[d]:
                vol = (d-i) * min([heights[i], heights[d]])
                if vol > max_vol:
                    max_vol = vol
                i+=1
            while heights[d] < heights[i]:
                vol = (d-i) * min([heights[i], heights[d]])
                if vol > max_vol:
                    max_vol = vol
                d-=1
            if heights[d] == heights[i]:
                vol = (d-i) * min([heights[i], heights[d]])
                if vol > max_vol:
                    max_vol = vol
                if heights[d-1] > heights[d]:
                    d-=1
                else:
                    i+=1

        return max_vol
