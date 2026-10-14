class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n)
        dp[0] = cost[n - 1]
        dp[1] = cost[n - 2]
        for sA in range(2, n):
            dp[sA] = cost[n - 1 - sA] + min(dp[sA - 1], dp[sA - 2])
        return min(dp[-1], dp[-2]) # [0] = 1, [1] = 1, [2] = 3