class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        i=0

        for d in range(n):

            if prices[d]<prices[i]:
                i = d

            profit = prices[d] - prices[i]
            if profit > res:
                res = profit

        return res
        