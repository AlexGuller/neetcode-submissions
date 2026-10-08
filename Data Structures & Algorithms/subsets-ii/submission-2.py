class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort to make removing dupes easier
        nums.sort() # 1, 1, 2
        res = []

        def backtrack(currArr, start):
            res.append(currArr.copy())
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                # dont include dupes
                if i > start and nums[i] == nums[i - 1]:
                    continue
                currArr.append(nums[i])
                backtrack(currArr, i + 1) # start after the one we included
                currArr.pop()
        backtrack([], 0)
        return res
