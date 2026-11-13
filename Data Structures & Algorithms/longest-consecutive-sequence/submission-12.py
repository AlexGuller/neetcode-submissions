class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set()
        for n in nums:
            st.add(n)
        maxCount = 0
        for n in nums:
            currCount = 1
            if n in st:
                st.remove(n)
                rt = n
                lt = n
                # right
                while len(st) > 0 and rt + 1 in st:
                    rt = rt + 1
                    st.remove(rt)
                    currCount += 1
                #left
                while len(st) > 0 and lt - 1 in st:
                    lt = lt - 1
                    st.remove(lt)
                    currCount += 1
                maxCount = max(maxCount, currCount)
        return maxCount