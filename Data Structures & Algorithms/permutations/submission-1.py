class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtrack
        res = []
        seen = set()
        def backtrack(currArr, seen):
            if len(currArr) == len(nums):
                res.append(currArr.copy())
                return
            
            for i in range(len(nums)):
                if i not in seen:
                    seen.add(i)
                    currArr.append(nums[i])
                    backtrack(currArr, seen)
                    seen.remove(i)
                    currArr.pop()
        backtrack([], seen)
        return res