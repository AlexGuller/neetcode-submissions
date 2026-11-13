class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        lt, rt = 0, 1
        mx = 1
        seen = set()
        seen.add(s[0])
        while rt < len(s):
            if s[rt] not in seen:
                seen.add(s[rt])
                mx = max(mx, len(seen))
                rt += 1
            else:
                while s[lt] != s[rt]:
                    seen.remove(s[lt])
                    lt += 1
                seen.remove(s[lt])
                lt += 1
        return mx