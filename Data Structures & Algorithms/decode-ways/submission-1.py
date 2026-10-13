class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(n):
            # cant ever have a 0 as start
            if s[n - 1 - i] == "0":
                dp[i + 1] = 0
            else:
                dp[i + 1] += dp[i]
            
            # 10-26 check
            if n - i < n and (s[n - 1 - i] == "1" or (s[n - 1 - i] == "2" and s[n - i] in "0123456")):
                dp[i + 1] += dp[i - 1]
        return dp[-1]