class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for i in range(len(nums) - 1):
            pre.append(pre[i] * nums[i])
        
        post = [1]
        for i in range(len(nums) - 1, 0, -1):
            post.append(post[len(nums) - 1 - i] * nums[i])
        
        res = []
        for i in range(len(post)):
            res.append(pre[i] * post[len(post) - 1 - i])
            # 1 1 2 8
            # 1 6 24 48
        
        return res