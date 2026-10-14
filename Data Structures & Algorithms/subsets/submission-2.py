class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(currArr, start):
            res.append(currArr.copy())
            if len(currArr) == len(nums):
                return
            
            for i in range(start, len(nums)):
                # remove doubles by only include copies behind us
                if i > start and nums[i] == nums[i - 1]:
                    continue
                currArr.append(nums[i])
                backtrack(currArr, i + 1)
                currArr.pop()
        backtrack([], 0)
        return res