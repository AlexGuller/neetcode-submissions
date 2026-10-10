class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for i in range(len(s)):
                arr[ord(s[i]) - ord('a')] += 1
            freq[tuple(arr)].append(s)
        return list(freq.values())