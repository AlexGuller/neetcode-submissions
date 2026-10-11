class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return sorted([i, seen[target - nums[i]]])
            seen[nums[i]] = i
        return [-1,-1]