class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIdx = {}
        lt = 0
        rt = 0
        maxLen = 0
        while rt < len(s):#a:0 b:2 -> lt=2 rt=3
            if s[rt] in lastIdx:
                lt = max(lt, lastIdx[s[rt]] + 1)
            lastIdx[s[rt]] = rt
            maxLen = max(maxLen, rt - lt + 1)
            rt += 1
        return maxLen