class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        r = 0
        while r < rows and target > matrix[r][cols - 1]:
            r += 1
        if r == rows:
            return False

        rt = cols - 1
        lt = 0
        mid = (rt + lt) // 2
        while lt <= rt:
            if matrix[r][mid] < target:
                lt = mid + 1
                mid = (rt + lt) // 2
            elif matrix[r][mid] > target:
                rt = mid - 1
                mid = (rt + lt) // 2
            elif matrix[r][mid] == target:
                return True
        return False
        