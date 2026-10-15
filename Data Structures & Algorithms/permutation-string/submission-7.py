class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        str1 = [0] * 26
        str2 = [0] * 26
        for i in range(len(s1)):
            str1[ord(s1[i]) - ord('a')] += 1
            str2[ord(s2[i]) - ord('a')] += 1
        
        l = 0
        r = len(s1) - 1
        if str1 == str2:
            return True
        while r < len(s2) - 1:
            str2[ord(s2[l]) - ord('a')] -= 1
            str2[ord(s2[r + 1]) - ord('a')] += 1
            l += 1
            r += 1
            if str1 == str2:
                return True
        return False