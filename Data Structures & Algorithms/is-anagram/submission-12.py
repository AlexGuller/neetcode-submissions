class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        aT = defaultdict(int)
        aS = defaultdict(int)
        for i in range(len(s)):
            aT[t[i]] += 1
            aS[s[i]] += 1
        return aT == aS
