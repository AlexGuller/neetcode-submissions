class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(currArr, start):
            res.append(currArr.copy())

            for i in range(start, len(nums)):
                # As you iterate through the array, you are able to use all repeats of numbers before you but not after you to ensure no duplicate arrays
                if i > start and nums[i] == nums[i - 1]:
                    continue
                currArr.append(nums[i])
                backtrack(currArr, i + 1)
                currArr.pop()
        backtrack([], 0)
        return res