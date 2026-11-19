class Solution:
    def rob(self, nums: List[int]) -> int:
        def helpRob(startIdx):
            lenRob = len(nums) - 1 + startIdx
            if lenRob == 1:
                return nums[startIdx]
            dp = [0] * lenRob
            # last house
            dp[lenRob - 1] = nums[lenRob - 1]
            # second to last
            dp[lenRob - 2] = max(nums[lenRob - 1], nums[lenRob - 2])
            for i in range(lenRob - 3, startIdx - 1, -1):
                dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
            return max(dp[0], dp[1])
        if len(nums) == 1:
            return nums[0]
        return max(helpRob(0), helpRob(1))