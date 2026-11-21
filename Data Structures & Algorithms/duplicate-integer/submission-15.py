class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for n in freq.values():
            if n > 1:
                return True
        return False