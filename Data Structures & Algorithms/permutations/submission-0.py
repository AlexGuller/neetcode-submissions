class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        def backtrack(seen, currArr):
            if len(currArr) == len(nums):
                res.append(currArr.copy())
                return
            for i in range(len(nums)):
                if i not in seen:
                    seen.add(i)
                    currArr.append(nums[i])
                    backtrack(seen, currArr)
                    currArr.pop()
                    seen.remove(i)
        backtrack(seen, [])
        return res