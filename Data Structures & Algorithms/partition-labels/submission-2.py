class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # last index map
        lI = {}
        for i in range(len(s)):
            lI[s[i]] = i
        
        # count
        res = []
        end = 0
        size = 0
        for i in range(len(s)):
            size += 1
            end = max(end, lI[s[i]])
            if i == end:
                res.append(size)
                size = 0
        return res