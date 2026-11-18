class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lt = 0
        rt = 0
        maxVal = 0
        while rt < len(prices):
            if prices[rt] < prices[lt]:
                lt = rt
            maxVal = max(prices[rt] - prices[lt], maxVal)
            rt += 1
        return maxVal