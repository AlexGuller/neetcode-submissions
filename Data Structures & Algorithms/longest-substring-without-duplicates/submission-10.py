class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lt, rt = 0, 0
        mx = 0
        seen = {}
        while rt < len(s):
            if s[rt] in seen:
                lt = max(lt, seen[s[rt]] + 1)
            seen[s[rt]] = rt
            rt += 1
            mx = max(mx, rt - lt)
        return mx