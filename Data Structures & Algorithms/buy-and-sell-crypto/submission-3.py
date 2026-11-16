class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lt = 0
        rt = 0
        maxP = 0
        while rt < len(prices):
            if prices[rt] < prices[lt]:
                lt = rt
            maxP = max(maxP, prices[rt] - prices[lt])
            rt += 1
        return maxP