class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        ctr = 0
        while ctr < len(s):
            lenWord = ""
            while s[ctr] != "#":
                lenWord += s[ctr]
                ctr += 1
            ctr += 1
            lenWord = int(lenWord)
            decoded.append(s[ctr:ctr + lenWord])
            ctr += lenWord
        return decoded