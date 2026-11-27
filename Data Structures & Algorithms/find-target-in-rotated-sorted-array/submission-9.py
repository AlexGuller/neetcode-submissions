class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lt = 0
        rt = len(nums) - 1
        while lt <= rt:
            mid = (rt + lt) // 2
            if target == nums[mid]:
                return mid
            # left sorted
            if nums[lt] <= nums[mid]:
                if nums[lt] <= target < nums[mid]:
                    rt = mid - 1
                else:
                    lt = mid + 1
            # right sorted
            if nums[rt] >= nums[mid]:
                if nums[rt] >= target > nums[mid]:
                    lt = mid + 1
                else:
                    rt = mid - 1
        return -1