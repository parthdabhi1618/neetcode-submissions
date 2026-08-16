class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<1:
            return 0
        l=r=0
        max_profit=float("-inf")
        while r<len(prices)-1:
            r+=1
            max_profit=max(prices[r]-prices[l],max_profit)
            if prices[r]<=prices[l]:
                l=r
        if max_profit<=0:
            return 0
        return max_profit