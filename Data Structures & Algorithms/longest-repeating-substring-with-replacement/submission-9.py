class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = 0
        freq = defaultdict(int)
        lt, rt = 0, 0
        maxLen = 0
        while rt < len(s):
            freq[s[rt]] += 1
            maxFreq = max(maxFreq, freq[s[rt]])
            while lt < rt and rt - lt + 1 - maxFreq > k:
                freq[s[lt]] -= 1
                lt += 1
            currLen = rt - lt + 1
            maxLen = max(maxLen, currLen)
            rt += 1
        return maxLen