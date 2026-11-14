class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqT = Counter(t)
        freqS = Counter(s)
        return freqT == freqS