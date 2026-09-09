class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        m = {"(":")","[":"]","{":"}"}
        for ch in s:
            if ch in m:
                st.append(ch)
            elif len(st) != 0 and ch == m[st[-1]]:
                st.pop()
            else:
                return False
        return len(st) == 0