class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # from the ith floor
        # can step 1 or 2 steps after paying
        # return min 1 or 0
        dp = [0] * len(cost)
        
        # from top can only step 1
        dp[len(cost) - 1] = cost[len(cost) - 1]
        # from top - 1 can step 1(to next step) or 2(top of floor)
        # always cheapest to jump straight to top
        dp[len(cost) - 2] = cost[len(cost) - 2]
        for i in range(len(cost) - 3, -1, -1):
            # curr cost + 1 step cost or 2 step cost
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])