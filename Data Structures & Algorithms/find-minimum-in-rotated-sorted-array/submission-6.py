class Solution:
    def findMin(self, nums: List[int]) -> int:
        lt = 0
        rt = len(nums) - 1
        while lt < rt:
            mid = (rt + lt) // 2
            if nums[mid] > nums[rt]:
                lt = mid + 1
            else:
                rt = mid
        return nums[lt]