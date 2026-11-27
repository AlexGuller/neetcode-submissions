class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        last = float('infinity')
        for i in range(len(prices)):
            if prices[i] > last:
                best = max(best, prices[i] - last)
            else:
                last = prices[i]
        return best