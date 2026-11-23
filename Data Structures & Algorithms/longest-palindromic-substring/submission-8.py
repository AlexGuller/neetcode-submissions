class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        # left and right from each letter
        def isPaliOne(startIdx):
            temp = s[startIdx]
            lt = startIdx - 1
            rt = startIdx + 1
            while lt >= 0 and rt <= len(s) - 1:
                if s[lt] == s[rt]:
                    temp = s[lt] + temp + s[rt]
                    lt -= 1
                    rt += 1
                else:
                    break
            return temp
        def isPaliTwo(startIdx):
            temp = s[startIdx] + s[startIdx - 1]
            lt = startIdx - 2
            rt = startIdx + 1
            while lt >= 0 and rt <= len(s) - 1:
                if s[lt] == s[rt]:
                    temp = s[lt] + temp + s[rt]
                    lt -= 1
                    rt += 1
                else:
                    break
            return temp
        
        maxString = ""
        for i in range(1, len(s)):
            currWordOne = isPaliOne(i)
            if len(currWordOne) > len(maxString):
                maxString = currWordOne
            if s[i] == s[i - 1]:
                currWordTwo = isPaliTwo(i)
                if len(currWordTwo) > len(maxString):
                    maxString = currWordTwo
        return maxString