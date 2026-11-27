class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIdx = {}
        lt = rt = 0
        maxCounter = 0
        while rt < len(s):
            if s[rt] in lastIdx:
                lt = max(lt, lastIdx[s[rt]] + 1)
            lastIdx[s[rt]] = rt
            maxCounter = max(maxCounter, rt - lt + 1)
            rt += 1
        return maxCounter