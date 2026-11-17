class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # each time we can choose open or closed
        # if we have the maximum amount of open, no more open added
        res = []
        def backtrack(oP, cP, currStr):
            if oP == n and oP == cP:
                res.append(currStr)
                return
            if oP < n:
                tempO = currStr + '('
                backtrack(oP + 1, cP, tempO)
            if cP < oP:
                tempC = currStr + ')'
                backtrack(oP, cP + 1, tempC)
        backtrack(0, 0, "")
        return res