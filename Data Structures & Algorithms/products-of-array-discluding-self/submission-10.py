class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for i in range(1, len(nums)):
            pre.append(pre[i - 1] * nums[i - 1])
        post = 1
        for i in range(len(nums) - 2, -1, -1):#[1, 2, 8, 48]
            pre[i] *= post * nums[i + 1]
            post *= nums[i + 1]
        return pre