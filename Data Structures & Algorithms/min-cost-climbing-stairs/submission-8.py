class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[n - 1]
        dp[1] = cost[n - 2]
        for i in range(2, n):
            dp[i] = cost[n - 1 - i] + min(dp[i - 1], dp[i - 2])
        return min(dp[-1], dp[-2])