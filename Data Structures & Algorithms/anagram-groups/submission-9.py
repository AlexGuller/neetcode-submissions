class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key is array 26 of chars
        freq = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for ch in s:
                key[ord(ch) - ord('a')] += 1
            freq[tuple(key)].append(s)
        res = list(freq.values())
        return res