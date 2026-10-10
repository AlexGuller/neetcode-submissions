class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        arr = sorted(freq.keys(), key=lambda c:freq[c], reverse=True)
        return arr[:k]