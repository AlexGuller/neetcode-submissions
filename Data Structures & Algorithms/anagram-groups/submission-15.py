class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        group = collections.defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for ch in word:
                arr[ord(ch) - ord('a')] += 1
            group[tuple(arr)].append(word)
        return [v for v in group.values()]