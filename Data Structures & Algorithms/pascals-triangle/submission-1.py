class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        dp = []
        dp.append([1])
        dp.append([1, 1])
        for i in range(2, numRows):
            arr = [1]
            for prevVal in range(1, len(dp[i - 1])): # 1, 1
                arr.append(dp[i - 1][prevVal] + dp[i - 1][prevVal - 1])
            arr.append(1)
            dp.append(arr)
        return dp

