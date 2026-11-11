class Solution:

    def encode(self, strs: List[str]) -> str:
        # 5#str
        encoded = ""
        for s in strs:
            encoded += str(len(s))
            encoded += "#"
            encoded += s
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        ctr = 0
        while ctr < len(s):
            numStr = ""
            while s[ctr] != "#":
                numStr += s[ctr]
                ctr += 1
            ctr += 1
            decoded.append(s[ctr:ctr + int(numStr)])
            ctr += int(numStr)
        return decoded