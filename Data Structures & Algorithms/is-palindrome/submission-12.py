class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s) - 1
        l = 0
        while l <= r:
            while l < r and not s[r].isalnum():
                r -= 1
            while l < r and not s[l].isalnum():
                l += 1
            if s[r].casefold() != s[l].casefold():
                return False
            r -= 1
            l += 1
        return True