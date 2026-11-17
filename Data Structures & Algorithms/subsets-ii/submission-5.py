class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        def backtrack(currArr, startIdx):
            if startIdx == len(nums):
                return
            for i in range(startIdx, len(nums)):
                if i > startIdx and nums[i] == nums[i - 1]:
                    continue
                currArr.append(nums[i])
                res.append(currArr.copy())
                backtrack(currArr, i + 1)
                currArr.pop()
                # 2 2 2 2 5 6
        backtrack([], 0)
        return res