class Solution:
    def isValid(self, s: str) -> bool:
        match = {'}':'{', ']':'[', ')':'('}
        st = []
        for ch in s:
            if ch not in match:
                st.append(ch)
            elif ch in match and (len(st) == 0 or st[-1] != match[ch]):
                return False
            else:
                st.pop()
        return len(st) == 0