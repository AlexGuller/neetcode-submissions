class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        # aabddert
        def isPalindrome(word):
            lt = 0
            rt = len(word) - 1
            while lt <= rt:
                if word[lt] != word[rt]:
                    return False
                lt += 1
                rt -= 1
            return True

        def backtrack(startIdx, currArr, totInArr):
            if totInArr == len(s):
                res.append(currArr.copy())
                return
            for i in range(startIdx, len(s)):
                currWord = s[startIdx:i + 1]
                if isPalindrome(currWord):
                    currArr.append(currWord)
                    backtrack(i + 1, currArr, totInArr + i + 1 - startIdx)
                    currArr.pop()
            return
        backtrack(0, [], 0)
        return res
