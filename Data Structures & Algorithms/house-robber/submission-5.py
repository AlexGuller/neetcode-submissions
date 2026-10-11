class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)

        # base case there is one house -> we rob it
        dp[0] = nums[len(nums) - 1]

        # base case there are two houses -> we rob only this one
        dp[1] = max(nums[len(nums) - 2], dp[0])

        for i in range(2, len(nums)):
            # can either rob this one and skip a house and rob
            # OR
            # can rob house in front
            dp[i] = max(dp[i - 1], nums[len(nums) - 1 - i] + dp[i - 2])
        return dp[len(dp) - 1]