class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkPali(start, end):
            l = start
            r = end
            temp = ""
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if l == r:
                    temp = s[l]
                else:
                    temp = s[l] + temp + s[r]
                l -= 1
                r += 1
            return temp
            
        sMx = s[0]
        for i in range(len(s) - 1):
            tempE = checkPali(i, i + 1)
            tempO = checkPali(i, i)
            if len(tempO) > len(sMx):
                sMx = tempO
            if len(tempE) > len(sMx):
                sMx = tempE
        return sMx
        