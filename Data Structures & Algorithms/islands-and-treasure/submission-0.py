class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        q = deque()
        for rows in range(len(grid)):
            for cols in range(len(grid[0])):
                if grid[rows][cols] == 0:
                    q.append((rows, cols))
        
        while q:
            row, col = q.popleft()
            # left wall
            if col - 1 >= 0 and grid[row][col - 1] == INF:
                grid[row][col - 1] = grid[row][col] + 1
                q.append((row, col - 1))
            # ceiling
            if row - 1 >= 0 and grid[row - 1][col] == INF:
                grid[row - 1][col] = grid[row][col] + 1
                q.append((row - 1, col))
            # floor 
            if row + 1 < len(grid) and grid[row + 1][col] == INF:
                grid[row + 1][col] = grid[row][col] + 1
                q.append((row + 1, col))
            # right wall 
            if col + 1 < len(grid[0]) and grid[row][col + 1] == INF:
                grid[row][col + 1] = grid[row][col] + 1
                q.append((row, col + 1))
        