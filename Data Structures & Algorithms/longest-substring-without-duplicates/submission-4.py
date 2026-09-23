class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        l = 0
        r = 1
        mL = 1
        seen = set()
        seen.add(s[l])
        while r < len(s):
            if s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
                r += 1
                mL = max(mL, r - l)
        mL = max(mL, r - l)
        return mL