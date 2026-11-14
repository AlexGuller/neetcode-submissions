class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lt = 0
        rt = 0
        mx = 0
        while rt < len(prices):
            mx = max(mx, prices[rt] - prices[lt])
            if prices[lt] > prices[rt]:
                lt = rt
            rt += 1
            print(rt)
        return mx