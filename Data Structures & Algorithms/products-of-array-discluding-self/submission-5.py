class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #pre
        prefix = [1]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i - 1])

        #post len - 1 - len + 3 - 1= 0
        postfix = [1]
        end = len(nums) - 1
        for i in range(end - 1, -1, -1):
            postfix.append(postfix[(end - i - 1)] * nums[i + 1])
        
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[len(nums) - 1 - i])
        return res