class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sortedArr = sorted(freq.keys(), key=lambda k:freq[k])
        return sortedArr[-k:]