class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, arr, tot):
            if tot == target:
                res.append(arr.copy())
                return
            if tot > target or idx >= len(nums):
                return
            arr.append(nums[idx])
            dfs(idx, arr, tot + nums[idx])
            arr.pop()
            dfs(idx + 1, arr, tot)

        dfs(0, [], 0)
        return res