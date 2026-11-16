class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # start at biggest number and keep adding until overshot
        # chop until
        
        nums.sort()
        res = []
        def backtrack(tot, currIdx, currArr):
            if tot == target:
                res.append(currArr.copy())
            for i in range(currIdx, len(nums)):
                if tot > target:
                    break
                currArr.append(nums[i])
                backtrack(tot + nums[i], i, currArr)
                currArr.pop()
                
        backtrack(0, 0, [])
        return res
            