class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        arr = sorted(freq.keys(), key=lambda n:freq[n], reverse=True)
        return arr[:k]