class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        mx = 0
        for n in nums:
            nt = n
            temp = 1
            if n - 1 not in s:
                while nt + 1 in s:
                    temp += 1
                    nt += 1
                mx = max(mx, temp)
        return mx