class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(startIdx, currArr, tot):
            if tot == target:
                res.append(currArr.copy())
                return
            for i in range(startIdx, len(nums)):
                if tot + nums[i] > target:
                    break
                if i > startIdx and nums[i] == nums[i - 1]:
                    continue # 1 2 3 3
                currArr.append(nums[i])
                backtrack(i, currArr, tot + nums[i])
                currArr.pop()
            return
        backtrack(0, [], 0)
        return res