class Solution:
    def isValid(self, s: str) -> bool:
        match = {'}':'{', ']':'[', ')':'('}
        st = []
        for i in range(len(s)):
            if s[i] not in match:
                st.append(s[i])
            elif len(st) == 0 or st[-1] != match[s[i]]:
                return False
            else:
                st.pop()
        return len(st) == 0