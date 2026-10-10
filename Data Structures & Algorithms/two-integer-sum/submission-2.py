class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh = defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i] in hsh:
                return sorted([i, hsh[target - nums[i]]])
            hsh[nums[i]] = i
        return [-1, -1]