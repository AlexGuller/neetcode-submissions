class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in freq and i != freq[nums[i]]:
                return sorted([i, freq[nums[i]]])
        return [-1, -1]