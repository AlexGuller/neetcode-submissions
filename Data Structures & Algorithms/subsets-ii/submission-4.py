class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        res.append([])
        def backtrack(startIdx, currArr):
            for i in range(startIdx, len(nums)): # 7774
                if i > startIdx and nums[i] == nums[i - 1]:
                    continue
                currArr.append(nums[i])
                res.append(currArr.copy())
                backtrack(i + 1, currArr)
                currArr.pop()
            return
        backtrack(0, [])
        return res