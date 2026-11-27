class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i in range(len(nums)):
            idx[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in idx and idx[nums[i]] != i:
                return sorted([i, idx[nums[i]]])
        return [-1, -1]