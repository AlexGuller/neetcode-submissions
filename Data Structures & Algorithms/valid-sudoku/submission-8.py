class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(list)
        col = collections.defaultdict(list)
        box = collections.defaultdict(list)
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v != '.':
                    if v in row[r]:
                        return False
                    if v in col[c]:
                        return False
                    if v in box[(c // 3) + 3 * (r // 3)]:
                        return False
                    row[r].append(v)
                    col[c].append(v)
                    box[(c // 3) + 3 * (r // 3)].append(v)
        return True