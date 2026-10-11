class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        arr = sorted(freq.keys(), key=lambda k:freq[k], reverse=True)
        return arr[:k]