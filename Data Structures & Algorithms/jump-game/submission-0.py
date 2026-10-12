class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        dp = [False] * len(nums)
        # at end
        dp[0] = True

        for i in range(1, len(nums)):
            jS = nums[len(nums) - 1 - i]
            for j in range(1, min(jS, i) + 1):
                if dp[i - j]:
                    dp[i] = True
                    break
        return dp[len(nums) - 1]