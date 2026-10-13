class Solution:
    def countSubstrings(self, s: str) -> int:
        def checkPali(start, end):
            l = start
            r = end
            count = 0
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        ct = 1
        for i in range(len(s) - 1):
            ct += checkPali(i, i) + checkPali(i, i + 1)
        return ct