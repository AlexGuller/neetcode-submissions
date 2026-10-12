class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        idx = 1
        currVal = prices[0]
        tot = 0
        while idx < len(prices):
            # iterate to find next greatest
            if prices[idx] > currVal:
                mx = prices[idx] # 5
                while idx + 1 < len(prices) and prices[idx + 1] >= mx:
                    mx = prices[idx + 1]
                    idx += 1
                # update total and currVal
                tot += mx - currVal
            currVal = prices[idx]
            idx += 1
        return tot