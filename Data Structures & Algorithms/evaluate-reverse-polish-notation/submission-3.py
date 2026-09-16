class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                val2 = int(st.pop())
                val1 = int(st.pop())
                st.append(int(val1 + val2))
            elif tokens[i] == '-':
                val2 = int(st.pop())
                val1 = int(st.pop())
                st.append(int(val1 - val2))
            elif tokens[i] == '/':
                val2 = int(st.pop())
                val1 = int(st.pop())
                st.append(int(val1 / val2))
            elif tokens[i] == '*':
                val2 = int(st.pop())
                val1 = int(st.pop())
                st.append(int(val1 * val2))
            else:
                st.append(int(tokens[i]))
        return st.pop()