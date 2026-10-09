class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        def backtrack(currArr, seen):
            if len(currArr) == len(nums):
                res.append(currArr.copy())
            for n in nums:
                if n not in seen:
                    seen.add(n)
                    currArr.append(n)
                    backtrack(currArr, seen)
                    seen.remove(n)
                    currArr.pop()
        backtrack([], seen)
        return res