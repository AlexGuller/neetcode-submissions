class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        sPtr = len(s) - 1
        tPtr = len(t) - 1
        while tPtr >= 0 and sPtr >= 0:
            if t[tPtr] == s[sPtr]:
                sPtr -= 1
            tPtr -= 1
        return sPtr == -1