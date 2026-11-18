class Solution:
    def isValid(self, s: str) -> bool:
        vals = {'}':'{',')':'(', ']':'['}
        st = []
        for ch in s:
            if ch not in vals:
                st.append(ch)
            elif not st or vals[ch] != st[-1]:
                return False
            else:
                st.pop()
        return len(st) == 0
