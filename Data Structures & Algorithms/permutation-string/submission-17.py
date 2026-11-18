class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freqS1 = Counter(s1)
        freqS2 = defaultdict(int)
        for i in range(len(s1)):
            freqS2[s2[i]] += 1
        for i in range(len(s1), len(s2)):
            if freqS1 == freqS2:
                return True
            freqS2[s2[i]] += 1
            freqS2[s2[i - len(s1)]] -= 1
            if freqS2[s2[i - len(s1)]] == 0:
                del freqS2[s2[i - len(s1)]]
        if freqS1 == freqS2:
            return True
        return False