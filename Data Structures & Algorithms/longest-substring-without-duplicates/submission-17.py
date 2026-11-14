class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIdx = {}
        mx = 0
        lt, rt = 0, 0
        while rt < len(s):
            if s[rt] in lastIdx:
                lt = max(lt, lastIdx[s[rt]] + 1)
            mx = max(mx, rt - lt + 1)
            lastIdx[s[rt]] = rt
            rt += 1
        return mx