class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        storeBoard = board
        def backtrack(r, c, currLetterIdx):
            if currLetterIdx == len(word):
                return True
            #if explored all options
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[currLetterIdx]:
                return False
            #mark visited cell and store original board
            temp = board[r][c]
            board[r][c] = "#"

            found = backtrack(r - 1, c, currLetterIdx + 1) or backtrack(r + 1, c, currLetterIdx + 1) or backtrack(r, c - 1, currLetterIdx + 1) or backtrack(r, c + 1, currLetterIdx + 1)

            board[r][c] = temp
            return found
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False