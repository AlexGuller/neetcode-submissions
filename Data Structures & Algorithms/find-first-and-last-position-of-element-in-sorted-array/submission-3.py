class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                tL = mid
                tR = mid
                while tL - 1 > -1 and nums[tL - 1] == target:
                    tL -= 1
                while tR + 1 < len(nums) and nums[tR + 1] == target:
                    tR += 1 
                return [tL, tR]
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return [-1, -1]