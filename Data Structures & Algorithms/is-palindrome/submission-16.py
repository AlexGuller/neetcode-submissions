class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnumString = ""
        for ch in s:
            if ch.isalnum():
                alnumString += ch.lower()
        return alnumString == alnumString[::-1]