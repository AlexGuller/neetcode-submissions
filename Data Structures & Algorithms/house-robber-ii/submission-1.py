class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(nums):
            if len(nums) == 1:
                return nums[0]
            dp = [0] * len(nums)

            # base cases
            # rob last house
            dp[0] = nums[len(nums) - 1]
            # rob second to last house or last house
            dp[1] = max(nums[len(nums) - 2], dp[0])

            for i in range(2, len(nums)):
                # rob this house and skip a house and rob
                # OR
                # rob next house only
                dp[i] = max(dp[i - 1], nums[len(nums) - 1 - i] + dp[i - 2])
            return dp[len(dp) - 1]
        return max(helper(nums[1:len(nums)]), helper(nums[0:len(nums) - 1]))