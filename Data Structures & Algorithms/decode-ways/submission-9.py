class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        dp[0] = 1 if s[n - 1] != "0" else 0
        for i in range(1, len(s)):
            if s[n - 1 - i] != "0":
                dp[i] = dp[i - 1] # 1777: [0] = 1, [1] = 1, [2] = 1, [3] = 1
            
            if s[n - 1 - i] == "1" or s[n - 1 - i] == "2" and s[n - i] in "0123456":
                dp[i] += dp[i - 2] if i > 1 else 1
        return dp[-1]