class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        st = []
        for i in range(len(temperatures)):
            while len(st) != 0 and temperatures[st[-1]] < temperatures[i]:
                index = st.pop() # 38, 30,  -> 36, 35, 40
                result[index] = i - index
            st.append(i)
        return result