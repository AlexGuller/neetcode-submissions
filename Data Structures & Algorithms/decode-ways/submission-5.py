class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * len(s)
        dp[0] = 1 if s[n - 1] != "0" else 0
        for i in range(1, len(s)):
            # if zero then no ways
            if s[n - 1 - i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i - 1] # 226: [0] = 1, [1] = 0, [2] = 1
            
            # if we have a 1-> always going to be 2 added
            # if we have a 2 -> going to be 2 added when value 0-6 before
            if s[n - 1 - i] == "1" or s[n - 1 - i] == "2" and s[n - i] in "0123456":
                dp[i] += dp[i - 2] if i > 1 else 1
        return dp[-1]