class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for i in range(1, len(nums)):
            pre.append(pre[i - 1] * nums[i - 1])
        post = 1
        for i in range(len(nums) - 2, -1, -1):
            post *= nums[i + 1]
            pre[i] = post * pre[i]
        return pre