class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(start, currArr, remaining):
            if remaining == 0:
                res.append(currArr.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if remaining - candidates[i] >= 0:
                    currArr.append(candidates[i])
                    backtrack(i + 1, currArr, remaining - candidates[i])
                    currArr.pop()
        backtrack(0, [], target)
        return res