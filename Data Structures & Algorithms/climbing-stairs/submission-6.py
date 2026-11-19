class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n)
        # 1 step away
        dp[n - 1] = 1
        # 2 steps away
        dp[n - 2] = 2
        # 3 steps away and more
        for i in range(n - 3, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]