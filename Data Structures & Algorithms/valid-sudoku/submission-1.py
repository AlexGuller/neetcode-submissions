class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 sets for row col box
        # box index is ((row / 3) * 3) + (col % 3)

        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)
        for i in range(9):
            for j in range(9):
                string = board[i][j]
                if string == '.':
                    continue
                if (string in rows[i]) or (string in cols[j]) or (string in box[(i // 3) * 3 + (j // 3)]):
                    return False
                rows[i].add(string)
                cols[j].add(string)
                box[(i // 3) * 3 + (j // 3)].add(string)
        return True
