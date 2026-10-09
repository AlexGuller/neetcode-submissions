class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # find total of all numbers
        tot = 0
        for n in nums:
            tot += n
        
        # backtrack by subtracting and building a new total for all subsets
        usedIdxs = set()
        def backtrack(usedIdxs, total, build):
            if total == build:
                return True
            if len(usedIdxs) == len(nums):
                return False
            for i in range(len(nums)):
                if i not in usedIdxs:
                    usedIdxs.add(i)
                    if backtrack(usedIdxs, total - nums[i], build + nums[i]):
                        return True
                    usedIdxs.remove(i)
            return False
        return backtrack(usedIdxs, tot, 0)