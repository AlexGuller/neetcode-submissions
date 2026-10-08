class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total = 0
        seen = set()
        heap = [(0, 0)] # cost, idx -> cost first because that is what we are sorting by
        # iterate until we have visited everything
        while len(seen) < len(points):
            temp = heapq.heappop(heap)
            cost = temp[0]
            idx = temp[1]
            if idx in seen:
                continue
            seen.add(idx)
            total += cost
            for i in range(len(points)):
                if i not in seen:
                    ptCost = abs(points[i][0] - points[idx][0]) + abs(points[i][1] - points[idx][1])
                    heapq.heappush(heap, (ptCost, i))
        return total