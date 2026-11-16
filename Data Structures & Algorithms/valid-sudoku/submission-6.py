class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    if val in row[r]:
                        return False
                    if val in col[c]:
                        return False
                    if val in box[c//3 + (3*(r//3))]:
                        return False
                    box[c//3 + (3*(r//3))].add(val)
                    row[r].add(val)
                    col[c].add(val)
        return True