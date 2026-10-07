class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPtr = 0
        tPtr = 0
        while sPtr < len(s) and tPtr < len(t):
            if s[sPtr] == t[tPtr]:
                sPtr += 1
            tPtr += 1
        return sPtr == len(s)