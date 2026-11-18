class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIdx = {}
        lt = 0
        rt = 0
        maxStr = 0
        while rt < len(s):
            currLet = s[rt]
            if currLet in lastIdx:
                lt = max(lastIdx[currLet] + 1, lt)# 1
            lastIdx[currLet] = rt # 2
            maxStr = max(rt - lt + 1, maxStr)
            rt += 1
        return maxStr