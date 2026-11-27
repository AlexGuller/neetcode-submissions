class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        maxFreq = 0
        lt = rt = 0
        maxCount = 0
        while rt < len(s):
            freqs[s[rt]] += 1
            maxFreq = max(maxFreq, freqs[s[rt]])
            while rt - lt + 1 - maxFreq > k:
                freqs[s[lt]] -= 1
                lt += 1
            maxCount = max(maxCount, rt - lt + 1)
            rt += 1
        return maxCount