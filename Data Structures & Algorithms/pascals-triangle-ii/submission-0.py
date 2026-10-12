class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        dp = []
        dp.append([1])
        dp.append([1, 1])

        for i in range(2, rowIndex + 1):
            arr = [1]
            for j in range(1, len(dp[i - 1])):
                arr.append(dp[i - 1][j - 1] + dp[i - 1][j])
            arr.append(1)
            dp.append(arr)

        return dp[len(dp) - 1]