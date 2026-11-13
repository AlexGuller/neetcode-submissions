class Solution:
    def isPalindrome(self, s: str) -> bool:
        an = ""
        for ch in s:
            if ch.isalnum():
                an += ch.lower()
        return an == an[::-1]