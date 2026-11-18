class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sort = sorted(freq.keys(), key= lambda k:freq[k])
        return sort[-k:]