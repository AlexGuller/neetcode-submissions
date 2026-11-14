class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIdx = {}
        mx = 0
        lt, rt = 0, 0
        while rt < len(s):#pw
            if s[rt] in lastIdx:
                lt = max(lastIdx[s[rt]] + 1, lt)
            
            lastIdx[s[rt]] = rt
            mx = max(mx, rt - lt + 1)
            rt += 1
        return mx