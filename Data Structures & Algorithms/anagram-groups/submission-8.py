class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        seen = defaultdict(list)
        for word in strs:
            seen["".join(sorted(word))].append(word)
        return list(seen.values())