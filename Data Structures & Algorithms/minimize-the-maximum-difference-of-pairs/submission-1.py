class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def isValid(m):
            idx = 0
            count = 0
            while idx < len(nums) - 1:
                if abs(nums[idx] - nums[idx + 1]) <= m:
                    count += 1
                    idx += 1
                if count == p:
                    return True
                idx += 1
            return False
        if p == 0:
            return 0
        nums.sort()
        l = 0
        r = 10**9
        res = 0
        while l <= r:
            m = (l + r) // 2
            if isValid(m):
                r = m - 1
                res = m
            else:
                l = m + 1
        return res