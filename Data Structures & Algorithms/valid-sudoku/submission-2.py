class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for each square
            # check in itself square
            # check row 
            # check col
        
        # indice for sqaure is: check by doing 1pt in each dir
            # first mid: [1,1]
            # second mid: [1, 4]
            # third mid: [1, 7]
        
        box = defaultdict(set)
        row = defaultdict(set)
        col = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    if val in row[r]:
                        return False
                    if val in col[c]:
                        return False
                    boxVal = c // 3 + (3 * (r // 3))
                    if val in box[boxVal]:
                        return False
                    row[r].add(val)
                    col[c].add(val)
                    box[boxVal].add(val)
        return True