class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            m[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in m and m[nums[i]] != i:
                return sorted([i, m[nums[i]]])
        return [-1, -1]