class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq1 = Counter(s1)
        freq2 = defaultdict(int)
        for i in range(len(s1)):
            freq2[s2[i]] += 1
        if freq2 == freq1:
            return True
        for i in range(len(s1), len(s2)):
            freq2[s2[i - len(s1)]] -= 1
            if freq2[s2[i - len(s1)]] == 0:
                del freq2[s2[i - len(s1)]]
            freq2[s2[i]] += 1
            if freq2 == freq1:
                return True
        return False