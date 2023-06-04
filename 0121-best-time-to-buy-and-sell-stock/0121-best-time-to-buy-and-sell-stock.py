class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        maxp = 0
        
        while r < len(prices):
            p1, p2 = prices[l], prices[r]
            if p1 < p2:
                profit = p2 - p1
                maxp = max(maxp, profit)
            else:
                l = r
            r += 1
            
        return maxp