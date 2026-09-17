class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        middle = (r + l) // 2
        while l <= r:
            if nums[middle] < target:
                l = middle + 1
                middle = (r + l) // 2
            elif nums[middle] > target:
                r = middle - 1
                middle = (r + l) // 2
            elif target == nums[middle]:
                return middle
        return -1