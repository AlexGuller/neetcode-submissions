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
                    boxNum = c // 3 + 3 * (r // 3)
                    if val in box[boxNum]:
                        return False
                    row[r].add(val)
                    col[c].add(val)
                    box[boxNum].add(val)
        return True