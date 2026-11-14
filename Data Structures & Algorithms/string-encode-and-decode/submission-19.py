class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        return s
    def decode(self, s: str) -> List[str]:
        res = []
        curr = 0
        while curr < len(s):
            lenWord = ""
            while s[curr] != "#":
                lenWord += s[curr]
                curr += 1
            curr += 1
            res.append(s[curr:curr + int(lenWord)])
            curr += int(lenWord)
        return res