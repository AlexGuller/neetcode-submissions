class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        counter = 0
        while counter < len(s2):
            # check first letter in, bound in, sorted equal
            if s2[counter] in s1 and counter + len(s1) <= len(s2) and sorted(s1) == sorted(s2[counter:(counter + len(s1))]):
                return True
            counter += 1
        return False
