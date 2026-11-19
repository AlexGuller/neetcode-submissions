class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]
        # if at last house can rob it
        dp[len(nums) - 1] = nums[len(nums) - 1]
        # if at second to last can rob it or skip and rob next
        dp[len(nums) - 2] = max(nums[len(nums) - 1], nums[len(nums) - 2])
        # if at third can rob curr + (curr + 2) or (curr + 1)
        for i in range(len(nums) - 3, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        return dp[0]