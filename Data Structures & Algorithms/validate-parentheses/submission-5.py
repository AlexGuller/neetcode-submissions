class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'}' : '{', ')': '(', ']':'['}
        st = []
        for i in range(len(s)):
            if s[i] in mp:
                if not st or st[-1] != mp[s[i]]:
                    return False
                else:
                    st.pop()
            else:
                st.append(s[i])
        return len(st) == 0