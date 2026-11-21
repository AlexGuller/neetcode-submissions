class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freqS1 = Counter(s1)
        freqS2 = collections.defaultdict(int)
        for i in range(len(s1)):
            freqS2[s2[i]] += 1
        for i in range(len(s1), len(s2)):
            if freqS2 == freqS1:
                return True
            freqS2[s2[i - len(s1)]] -= 1
            if freqS2[s2[i - len(s1)]] == 0:
                del freqS2[s2[i - len(s1)]]
            freqS2[s2[i]] += 1
        return freqS1 == freqS2