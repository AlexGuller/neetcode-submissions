class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for i in range(len(nums) - 1):
            pre.append(pre[i] * nums[i])
        # 0, 1, 3, 7, 

        post = [1]
        for i in range(len(nums) - 1, 0, -1):
            post.append(post[len(nums) - 1 - i] * nums[i])
        # 0, 6, 10, 12

        res = []
        for i in range(len(nums)):
            res.append(pre[i] * post[len(nums) - 1 - i])
        return res