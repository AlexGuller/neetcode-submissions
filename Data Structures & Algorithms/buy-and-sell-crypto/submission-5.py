class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lt = 0
        rt = 0
        maxProf = 0
        while rt < len(prices):
            maxProf = max(maxProf, prices[rt] - prices[lt])
            if prices[rt] < prices[lt]:
                lt = rt
            rt += 1
        return maxProf