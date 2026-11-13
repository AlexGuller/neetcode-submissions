class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        curr = 0
        while curr < len(s):
            wLen = ""
            while s[curr] != "#":
                wLen += s[curr]
                curr += 1
            wLen = int(wLen)
            curr += 1
            res.append(s[curr:curr + wLen])
            curr += wLen
        return res