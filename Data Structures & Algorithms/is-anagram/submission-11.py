class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        aT = [0] * 26
        aS = [0] * 26
        for i in range(len(s)):
            aT[ord(t[i]) - ord('a')] += 1
            aS[ord(s[i]) - ord('a')] += 1
        return aT == aS
