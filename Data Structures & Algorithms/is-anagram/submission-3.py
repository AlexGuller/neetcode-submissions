class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tMap = defaultdict(int)
        sMap = defaultdict(int)
        for i in range(len(s)):
            tMap[t[i]] += 1
            sMap[s[i]] += 1
        return sMap == tMap