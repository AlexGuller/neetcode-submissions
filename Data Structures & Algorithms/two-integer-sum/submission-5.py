class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            if target - nums[i] in visited:
                return sorted([i, visited[target - nums[i]]])
            else:
                visited[nums[i]] = i
        return []