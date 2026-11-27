class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i - 1])
        post = 1
        for i in range(len(nums) - 2, -1, -1):
            post = post * nums[i + 1]
            prefix[i] = prefix[i] * post
        return prefix