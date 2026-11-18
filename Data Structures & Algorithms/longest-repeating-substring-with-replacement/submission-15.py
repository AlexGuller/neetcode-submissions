class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        maxCharVal = 0
        longest = 0
        lt = 0
        rt = 0
        while rt < len(s):
            currLet = s[rt]
            freq[currLet] += 1
            maxCharVal = max(maxCharVal, freq[currLet])# 2
            while lt < rt and rt - lt + 1 - maxCharVal > k:
                freq[s[lt]] -= 1
                lt += 1
            longest = max(longest, rt - lt + 1)
            rt += 1
        return longest