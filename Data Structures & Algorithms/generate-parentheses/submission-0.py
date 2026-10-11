class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(currStr, openUsed, closedUsed):
            if closedUsed > openUsed or (len(currStr) == (n * 2) and openUsed != closedUsed):
                return
            if len(currStr) == (n * 2):
                res.append(currStr)
                return
            # next is open
            backtrack(currStr + '(', openUsed + 1, closedUsed)
            # next is closed
            backtrack(currStr + ')', openUsed, closedUsed + 1)
        backtrack("", 0, 0)
        return res