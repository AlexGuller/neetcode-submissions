class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])

        def backtrack(board, currLetterIdx, r, c):
            if currLetterIdx == len(word):
                return True
            # if out of bounds or not correct letter return
            if r < 0 or c < 0 or r >= self.rows or c >= self.cols or board[r][c] != word[currLetterIdx]:
                return False
            
            # options: up down left right 
            #( make sure to mark board so no repeats )
            currLet = board[r][c]
            board[r][c] = "#"
            if backtrack(board, currLetterIdx + 1, r + 1, c) or backtrack(board, currLetterIdx + 1, r, c + 1) or backtrack(board, currLetterIdx + 1, r - 1, c) or backtrack(board, currLetterIdx + 1, r, c - 1):
                return True
            board[r][c] = currLet

        for r in range(self.rows):
            for c in range(self.cols):
                if backtrack(board.copy(), 0, r, c):
                    return True
        return False

