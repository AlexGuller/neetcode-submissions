class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        freq = defaultdict(list)
        for s in strs:
            temp = "".join(sorted(s))
            freq[temp].append(s)
        for k,v in freq.items():
            res.append(v)
        return res