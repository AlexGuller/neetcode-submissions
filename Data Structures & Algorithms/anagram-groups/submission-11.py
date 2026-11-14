class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for ch in word:
                arr[ord(ch) - ord('a')] += 1
            m[tuple(arr)].append(word)
        res = []
        for v in m.values():
            res.append(v)
        return res