class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):
            seen = set()
            for j in range(i + 1, len(nums)):
                complement = -(nums[j] + nums[i])
                if complement in seen:
                    arr = sorted([nums[i], nums[j], complement])
                    res.add(tuple(arr))
                seen.add(nums[j])
        return list(list(triplet) for triplet in res)