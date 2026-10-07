class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(currTotal, currArr, currIdx):
            if currTotal == target:
                res.append(currArr.copy())
                return

            # Options: all other numbers are the options
            for i in range(currIdx, len(candidates)):
                if i > currIdx and candidates[i] == candidates[i - 1]:
                    continue
                if currTotal + candidates[i] > target:
                    break
                currArr.append(candidates[i])
                backtrack(currTotal + candidates[i], currArr, i + 1)
                currArr.pop()
        backtrack(0, [], 0)
        return res