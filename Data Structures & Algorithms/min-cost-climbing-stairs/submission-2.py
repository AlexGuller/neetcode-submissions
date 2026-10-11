class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0

        dp = [0] * len(cost)

        # base case we are at the top step -> no cost
        dp[0] = cost[len(cost) - 1]
        # base case we are at the second to top step -> only cost to get to the top
        dp[1] = cost[len(cost) - 2]

        for i in range(2, len(cost)):
            dp[i] = cost[len(cost) - 1 - i] + min(dp[i - 1], dp[i - 2])
        
        return min(dp[len(dp) - 1], dp[len(dp) - 2])