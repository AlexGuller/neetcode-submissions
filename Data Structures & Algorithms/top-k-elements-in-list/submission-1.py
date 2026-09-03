class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # buckets
        dic = [[] for _ in range(len(nums) + 1)]

        # frequency of each number
        freq = Counter(nums)

        # fill buckets
        for key, value in freq.items():
            dic[value].append(key)
        
        # loop to get k most
        result = []
        counter = k
        bucket = len(dic) - 1
        while counter > 0:
            if len(dic[bucket]) != 0:
                bucketIdx = len(dic[bucket]) - 1
                while bucketIdx >= 0 and counter > 0:
                    result.append(dic[bucket][bucketIdx])
                    counter -= 1
                    bucketIdx -= 1
            bucket -= 1
        return result


