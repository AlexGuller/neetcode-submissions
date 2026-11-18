class Solution:
    def isPalindrome(self, s: str) -> bool:
        anStr = ""
        for ch in s:
            if ch.isalnum():
                anStr += ch.lower()
        return anStr == anStr[::-1]