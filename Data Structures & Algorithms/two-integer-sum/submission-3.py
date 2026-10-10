class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] not in seen:
                seen[nums[i]] = i
            else:
                return sorted([i, seen[target - nums[i]]])
        return [-1, -1]