class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob2(arr):
            if len(arr) == 1:
                return arr[0]
            n = len(arr)
            dp = [0] * n
            dp[0] = arr[n - 1]
            dp[1] = max(arr[n - 2], dp[0])
            for i in range(2, n):
                dp[i] = max(dp[i - 2] + arr[n - 1 - i], dp[i - 1])
            return dp[-1]
        return max(rob2(nums[1:]), rob2(nums[:len(nums) - 1]))