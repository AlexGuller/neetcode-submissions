class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        # already at the top
        dp[0] = 0
        # one step away from top
        dp[1] = cost[len(cost) - 1]
        for i in range(2, len(cost) + 1):
            dp[i] = cost[len(cost) - i] + min(dp[i - 1], dp[i - 2])
        return min(dp[len(cost)], dp[len(cost) - 1])
        # [0, 3, 2, 3]
