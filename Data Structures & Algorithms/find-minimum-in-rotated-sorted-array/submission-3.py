class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find where digits start decreasing, that is your digit
        midR = (len(nums) // 2)
        midL = (len(nums) // 2) - 1 if len(nums) % 2 == 0 else (len(nums) // 2)
        if nums[midR] < nums[midL]:
            return nums[midR]
        while midL > 0 or midR < len(nums) - 1:
            if midL > 0:
                if nums[midL] < nums[midL - 1]:
                    return nums[midL]
                else:
                    midL -= 1
            if midR < len(nums) - 1:
                if nums[midR] > nums[midR + 1]:
                    return nums[midR + 1]
                else:
                    midR += 1
        if nums[len(nums) - 1] > nums[0]:
            return nums[0]
        else:
            return nums[len(nums) - 1]