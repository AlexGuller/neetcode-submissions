class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        notFound = set(nums)
        res = []
        def backtrack(notFound, currArr):
            if len(notFound) == 0:
                res.append(currArr.copy())
            for n in nums:
                if n in notFound:
                    notFound.remove(n)
                    currArr.append(n)
                    backtrack(notFound, currArr)
                    currArr.pop()
                    notFound.add(n)
        backtrack(notFound, [])
        return res