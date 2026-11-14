class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        box = defaultdict(list)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    if val in row[r]:
                        return False
                    if val in col[c]:
                        return False
                    boxVal = c // 3 + 3 * (r // 3)
                    if val in box[boxVal]:
                        return False
                    row[r].append(val)
                    col[c].append(val)
                    box[boxVal].append(val)
        return True