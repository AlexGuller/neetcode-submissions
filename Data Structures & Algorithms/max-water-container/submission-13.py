class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lt = 0
        rt = len(heights) - 1
        maxArea = min(heights[lt], heights[rt])*(len(heights) - 1)
        while lt <= rt:
            if heights[lt] < heights[rt]:
                lt += 1
            else:
                rt -= 1
            maxArea = max(maxArea, min(heights[lt], heights[rt])*(rt - lt))
        return maxArea