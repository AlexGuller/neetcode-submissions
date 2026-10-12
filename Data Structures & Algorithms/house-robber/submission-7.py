class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[len(nums) - 1]
        dp[1] = max(nums[len(nums) - 2], dp[0])
        for i in range(2, len(nums)):
            dp[i] = max(nums[len(nums) - 1 - i] + dp[i - 2], dp[i - 1])
        return dp[-1]