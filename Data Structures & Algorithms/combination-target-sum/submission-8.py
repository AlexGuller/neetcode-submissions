class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(tot, startIdx, currArr):
            if tot == target:
                res.append(currArr.copy())
            for i in range(startIdx, len(nums)):
                if tot + nums[i] <= target:
                    currArr.append(nums[i])
                    backtrack(tot + nums[i], i, currArr)
                    currArr.pop()
        backtrack(0, 0, [])
        return res