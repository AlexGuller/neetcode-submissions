class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        lt = 0
        rt = 0
        maxFreq = 0
        maxString = 0
        while rt < len(s):
            freq[s[rt]] += 1
            maxFreq = max(maxFreq, freq[s[rt]])
            while rt - lt + 1 - maxFreq > k:
                freq[s[lt]] -= 1
                lt += 1
            rt += 1
            maxString = max(maxString, rt - lt)
        return maxString