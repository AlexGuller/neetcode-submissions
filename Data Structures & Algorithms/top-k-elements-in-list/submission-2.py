class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = [[] for _ in range(len(nums) + 1)]
        freq = Counter(nums)
        for key, value in freq.items():
            dic[value].append(key)
        result = []
        for bucket in range(len(nums), 0, -1):
            for lst in (dic[bucket]):
                result.append(lst)
                if len(result) == k:
                    return result
        return result


