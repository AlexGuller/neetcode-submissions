class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnumStr = ""
        for ch in s:
            if ch.isalnum():
                alnumStr += ch.lower()
        return alnumStr == alnumStr[::-1]