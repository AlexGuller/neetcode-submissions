class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(currArr, tot, startIdx):
            if tot == target:
                res.append(currArr.copy())
                return
            for i in range(startIdx, len(nums)):
                if tot + nums[i] > target:
                    return
                if i > startIdx and nums[i] == nums[i - 1]:
                    continue
                currArr.append(nums[i])
                backtrack(currArr, tot + nums[i], i)
                currArr.pop()
        backtrack([], 0, 0)
        return res