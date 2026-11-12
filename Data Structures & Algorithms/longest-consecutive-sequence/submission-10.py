class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        mx = 0
        for i in range(len(nums)):
            if nums[i] in st:
                st.remove(nums[i])
                curr = nums[i]
                down = curr
                currMx = 1
                while len(st) > 0 and (curr + 1) in st:
                    curr += 1
                    st.remove(curr)
                    currMx += 1
                while len(st) > 0 and (down - 1) in st:
                    down -= 1
                    st.remove(down)
                    currMx += 1
                mx = max(currMx, mx)
        return mx
