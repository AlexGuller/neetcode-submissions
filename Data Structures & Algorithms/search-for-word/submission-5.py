class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(r, c, currBoard, wordIdx):
            if wordIdx == len(word):
                return True
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[wordIdx]:
                return False
            temp = currBoard[r][c]
            currBoard[r][c] = "#"
            if backtrack(r + 1, c, currBoard, wordIdx + 1) or backtrack(r, c + 1, currBoard, wordIdx + 1) or backtrack(r - 1, c, currBoard, wordIdx + 1) or backtrack(r, c - 1, currBoard, wordIdx + 1):
                return True
            currBoard[r][c] = temp
            return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, board.copy(), 0):
                    return True
        return False