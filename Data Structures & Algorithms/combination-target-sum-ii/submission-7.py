class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        seen = set()
        def backtrack(tot, currIdx, currArr):
            if tot == target:
                res.append(currArr.copy())
            i = currIdx
            while i < len(candidates):
                if tot > target:
                    break
                currArr.append(candidates[i])
                backtrack(tot + candidates[i], i + 1, currArr)
                currArr.pop()
                # skip any forward dupes 2,2,2,2,2,2
                while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                    i += 1
                i += 1
        backtrack(0, 0, [])
        return res