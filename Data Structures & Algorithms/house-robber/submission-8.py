class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[n - 1]
        dp[1] = max(nums[n - 2], dp[0])
        for i in range(2, n):
            dp[i] = max(nums[n - 1 - i] + dp[i - 2], dp[i - 1])
        return dp[-1]