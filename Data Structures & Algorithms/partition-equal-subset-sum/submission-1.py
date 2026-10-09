class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # find total of all numbers
        tot = 0
        for n in nums:
            tot += n
        
        # backtrack by subtracting and building a new total for all subsets
        def backtrack(start, total, build):
            if total == build:
                return True
            if start == len(nums):
                return False
            for i in range(start, len(nums)):
                if backtrack(i + 1, total - nums[i], build + nums[i]):
                    return True
            return False
        return backtrack(0, tot, 0)