class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        str1 = [0] * 26
        for ch in s1:
            str1[ord(ch) - ord('a')] += 1
        
        for i in range(len(s2)):
            if str1[ord(s2[i]) - ord('a')] > 0 and len(s2) - i >= len(s1):
                str2 = [0] * 26
                for j in range(i, i + len(s1)):
                    str2[ord(s2[j]) - ord('a')] += 1
                if str1 == str2:
                    return True
        return False