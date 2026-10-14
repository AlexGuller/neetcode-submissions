class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {} # store coins per iter

        def dfs(amt):
            if amt <= 0:
                return 0
            if amt in memo:
                return memo[amt]

            res = 1e9
            for coin in coins:
                val = amt - coin
                if val >= 0:
                    res = min(res, 1 + dfs(val))
            memo[amt] = res
            return res
        res = dfs(amount)
        return -1 if res >= 1e9 else res