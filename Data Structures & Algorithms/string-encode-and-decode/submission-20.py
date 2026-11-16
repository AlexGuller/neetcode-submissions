class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded
    def decode(self, s: str) -> List[str]:
        currIdx = 0
        res = []
        while currIdx < len(s):
            lenWord = ""
            while s[currIdx] != "#":
                lenWord += s[currIdx]
                currIdx += 1
            currIdx += 1
            lenWord = int(lenWord)
            res.append(s[currIdx:currIdx + lenWord])
            currIdx += lenWord
        return res