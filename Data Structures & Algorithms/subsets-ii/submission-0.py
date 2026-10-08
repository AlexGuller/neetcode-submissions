class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(currArr, startIndex):
            res.append(currArr.copy())

            # Options: all integers in front
            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i-1]:
                    continue

                currArr.append(nums[i])
                backtrack(currArr, i + 1)
                currArr.pop()
        backtrack([], 0)
        return res