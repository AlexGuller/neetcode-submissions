class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        return s
    def decode(self, s: str) -> List[str]:
        res = []
        ptr = 0
        while ptr < len(s):
            sz = 0
            while s[ptr] != '#':
                sz = sz * 10 + int(s[ptr])
                ptr += 1
            ptr += 1
            res.append(s[ptr:(ptr + sz)])
            ptr += sz
        return res