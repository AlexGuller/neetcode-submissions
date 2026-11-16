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
                cnt = 0
                while tot < target:
                    currArr.append(nums[i])
                    tot += nums[i]
                    backtrack(tot, i + 1, currArr)
                    cnt += 1
                for j in range(cnt):
                    tot -= currArr.pop()
        backtrack(0, 0, [])
        return res
            