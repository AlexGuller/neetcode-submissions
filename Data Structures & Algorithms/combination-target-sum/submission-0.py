class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(currIdx, currNums, currTotal):
            if target == currTotal:
                res.append(currNums.copy())
                return
            if currTotal > target or currIdx >= len(nums):
                return
            
            #explore adding the current
            currNums.append(nums[currIdx])
            dfs(currIdx, currNums, currTotal + nums[currIdx])
            #explore moving to next
            currNums.pop()
            dfs(currIdx + 1, currNums, currTotal)
        dfs(0, [], 0)
        return res