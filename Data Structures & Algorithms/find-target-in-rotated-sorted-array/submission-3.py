class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find target index in O(logn) time
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        # binary search both sides
        lP = 0
        rP = pivot - 1
        while lP <= rP:
            m = (lP + rP) // 2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                rP = m - 1
            else:
                lP = m + 1
        lP = pivot
        rP = len(nums) - 1
        while lP <= rP:
            m = (lP + rP) // 2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                rP = m - 1
            else:
                lP = m + 1
        return -1