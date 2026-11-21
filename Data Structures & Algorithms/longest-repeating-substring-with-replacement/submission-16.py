class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = collections.defaultdict(int)
        lt = 0
        rt = 0
        maxCtr = 0
        maxFreq = 0
        while rt < len(s):
            freq[s[rt]] += 1
            maxFreq = max(maxFreq, freq[s[rt]])
            while rt - lt + 1 - maxFreq > k:
                freq[s[lt]] -= 1
                maxFreq = max(maxFreq, freq[s[lt]])
                lt += 1
            maxCtr = max(rt - lt + 1, maxCtr)
            rt += 1
        return maxCtr