class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        mx = 0
        i = 1
        while i < len(prices):
            if prices[i] < mn:
                mn = prices[i]
            else:
                mx = max(mx, prices[i] - mn)
            i += 1
        return mx