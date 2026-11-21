class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIdx = {}
        lt = 0
        rt = 0
        maxCount = 0
        while rt < len(s):
            if s[rt] in lastIdx:
                lt = max(lt, lastIdx[s[rt]] + 1)
            lastIdx[s[rt]] = rt
            maxCount = max(maxCount, rt - lt + 1)
            rt += 1
        return maxCount