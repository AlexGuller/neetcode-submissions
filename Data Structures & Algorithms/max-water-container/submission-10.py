class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lt, rt = 0, len(heights) - 1
        maxArea = min(heights[lt], heights[rt]) * (len(heights) - 1)
        while lt < rt:
            if heights[rt] > heights[lt]:
                lt += 1
            else:
                rt -= 1
            currArea = (rt - lt) * min(heights[lt], heights[rt])
            maxArea = max(maxArea, currArea)
        return maxArea
