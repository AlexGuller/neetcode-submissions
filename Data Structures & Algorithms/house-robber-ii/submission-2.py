class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        def helper(n):
            dp = [0] * (len(n))
            dp[0] = n[len(n) - 1]
            dp[1] = max(n[len(n) - 2], dp[0])
            for i in range(2, len(n)):
                dp[i] = max(dp[i - 2] + n[len(n) - 1 - i], dp[i - 1])
            return dp[-1]
        return max(helper(nums[1:]), helper(nums[:len(nums) - 1]))