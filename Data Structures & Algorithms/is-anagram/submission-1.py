class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = Counter(s)
        counterT = Counter(t)
        if len(counterS) != len(counterT):
            return False

        for key in counterS.keys():
            if counterS.get(key) != counterT.get(key):
                return False
        return True