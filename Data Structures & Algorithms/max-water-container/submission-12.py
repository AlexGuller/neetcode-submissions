class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lt = 0
        rt = len(heights) - 1
        maxArea = rt * min(heights[lt], heights[rt])
        while lt < rt:
            maxArea = max(maxArea, (rt - lt)*(min(heights[lt], heights[rt])))
            if heights[lt] < heights[rt]:
                lt += 1
            else:
                rt -= 1
        return maxArea