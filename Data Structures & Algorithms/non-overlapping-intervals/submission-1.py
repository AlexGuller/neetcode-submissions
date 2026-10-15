class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by start time
        curr = intervals[0]
        cntrForwards = 0
        intervals.sort(key=lambda i : i[0])
        for i in range(1, len(intervals)):
            if curr[1] <= intervals[i][0]:
                curr = intervals[i]
            else:
                cntrForwards += 1
        
        curr = intervals[len(intervals) - 1]
        cntrBackwards = 0
        for i in range(len(intervals) - 2, -1, -1):
            if curr[0] >= intervals[i][1]:
                curr = intervals[i]
            else:
                cntrBackwards += 1
        return min(cntrForwards, cntrBackwards)