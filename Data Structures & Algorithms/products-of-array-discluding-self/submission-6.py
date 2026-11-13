class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix
        pre = [1] # [1, 2, 8, ]
        for i in range(1, len(nums)):
            pre.append(pre[i - 1] * nums[i - 1])
        
        #solve backwards
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            pre[i] *= post
            post *= nums[i]
        
        return pre