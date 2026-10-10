class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tMap = [0] * 26
        sMap = [0] * 26
        for i in range(len(s)):
            tMap[ord(t[i]) - ord('a')] += 1
            sMap[ord(s[i]) - ord('a')] += 1
        return sMap == tMap