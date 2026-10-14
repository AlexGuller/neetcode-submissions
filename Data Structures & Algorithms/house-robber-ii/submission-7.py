class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robSub(currHouses):
            if len(currHouses) == 1:
                return currHouses[0]
            n = len(currHouses)
            dp = [0] * n
            dp[0] = currHouses[n - 1]
            dp[1] = max(dp[0], currHouses[n - 2])
            for i in range(2, n):
                dp[i] = max(currHouses[n - 1 - i] + dp[i - 2], dp[i - 1])
            return dp[-1]
        return max(robSub(nums[:-1]), robSub(nums[1:]))