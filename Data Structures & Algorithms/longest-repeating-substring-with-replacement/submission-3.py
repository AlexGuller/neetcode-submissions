class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for ch in set(s):
            l = 0
            countSame = 0
            for r in range(len(s)):
                if s[r] == ch:
                    countSame += 1
                while (r - l + 1) - countSame > k:
                    if s[l] == ch:
                        countSame -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res