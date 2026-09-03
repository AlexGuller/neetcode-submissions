class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target, index
        map = {}
        for i in range(len(nums)):
            if nums[i] in map.keys():
                return [map.get(nums[i]), i]
            else:
                map[target - nums[i]] = i
        return [-1, -1]