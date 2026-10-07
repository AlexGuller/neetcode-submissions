class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # All will have an empty array included
        res = [[]]

        for n in nums:
            for i in range(len(res)):
                res.append(res[i] + [n])
        
        return list(res)