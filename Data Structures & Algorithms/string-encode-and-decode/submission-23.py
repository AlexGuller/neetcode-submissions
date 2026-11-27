class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + '#' + word
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        cntr = 0
        while cntr < len(s):
            lenWord = ""
            while s[cntr] != '#':
                lenWord += s[cntr]
                cntr += 1
            cntr += 1
            lenWord = int(lenWord)
            decoded.append(s[cntr:cntr + lenWord])
            cntr += lenWord
        return decoded