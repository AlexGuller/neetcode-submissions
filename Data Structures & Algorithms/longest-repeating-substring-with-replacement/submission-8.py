class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lt, rt = 0, 0
        maxF = 0
        freq = defaultdict(int)
        maxL = 0
        while rt < len(s):
            ch = s[rt]
            freq[ch] += 1
            maxF = max(maxF, freq[ch])
            currLen = rt - lt + 1
            if currLen - maxF > k:
                freq[s[lt]] -= 1
                lt += 1
            else:
                maxL = max(maxL, currLen)
            rt += 1
        return maxL