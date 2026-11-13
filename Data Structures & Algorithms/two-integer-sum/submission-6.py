class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            mp[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in mp and i != mp[nums[i]]:
                return sorted([i, mp[nums[i]]])
        return [-1,-1]