class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = sorted(freq, key=lambda k:freq[k])
        return res[(-1 * k):]