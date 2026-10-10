class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort() # 1, 2, 2, 2, 3
        mx = 1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] - 1 == nums[i - 1]:
                curr += 1
            else:
                curr = 1
            mx = max(mx, curr)
        return mx