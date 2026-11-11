class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = Counter(t)
        freq2 = Counter(s)
        return freq1 == freq2