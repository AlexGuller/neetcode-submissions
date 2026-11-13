class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lt = 0
        rt = len(heights) - 1
        maxHeight = max(heights[rt], heights[lt])
        maxArea = min(heights[lt], heights[rt]) * rt
        while lt < rt:
            if heights[rt] > heights[lt]:
                lt += 1
            else:
                rt -= 1
            area = min(heights[rt], heights[lt]) * (rt - lt)
            maxArea = max(maxArea, area)
        return maxArea
        