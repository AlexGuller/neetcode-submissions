class Solution:
    def climbStairs(self, n: int) -> int:
        # base cases of last and second to last steps
        # 2 -> 1, 1 -> 1, 0 -> 1 + 1
        dp = [1, 1]
        for i in range(0, n - 1):
            dp.append(dp[i] + dp[i + 1])
        return dp[len(dp) - 1]