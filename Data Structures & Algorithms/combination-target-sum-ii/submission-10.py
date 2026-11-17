class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(tot, startIdx, currArr):
            if tot == target:
                res.append(currArr.copy())
            for i in range(startIdx, len(candidates)):
                if tot + candidates[i] > target:
                    break # 1 2 2 2 2 
                if i > startIdx and candidates[i] == candidates[i - 1]:
                    continue
                currArr.append(candidates[i])
                backtrack(tot + candidates[i], i + 1, currArr)
                currArr.pop()
        backtrack(0, 0, [])
        return res
            