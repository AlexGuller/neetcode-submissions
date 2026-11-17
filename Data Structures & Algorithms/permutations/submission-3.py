class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(currArr, seen):
            if len(currArr) == len(nums):
                res.append(currArr.copy())
                return
            for n in nums:
                if n not in seen:
                    seen.add(n)
                    currArr.append(n)
                    backtrack(currArr, seen)
                    currArr.pop()
                    seen.remove(n)
            return
        backtrack([], set())
        return res
            