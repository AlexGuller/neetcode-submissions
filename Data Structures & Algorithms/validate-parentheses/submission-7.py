class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'}':'{', ']':'[', ')':'('}
        res = []
        for i in range(len(s)):
            if s[i] in mp:
                if not res or res[-1] != mp[s[i]]:
                    return False
                else:
                    res.pop()
            else:
                res.append(s[i])
        return len(res) == 0