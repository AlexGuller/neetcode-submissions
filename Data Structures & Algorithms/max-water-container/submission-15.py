class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currMax = 0
        lt = 0
        rt = len(heights) - 1
        while lt < rt:
            height = min(heights[lt], heights[rt])
            currMax = max(currMax, (rt - lt)*height)
            if heights[lt] > heights[rt]:
                rt -= 1
            else:
                lt += 1
        return currMax