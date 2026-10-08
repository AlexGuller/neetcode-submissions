class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        seen = set()
        heap = [(0, 0)] # connection cost, point idx
        total = 0
        while len(seen) < len(points):
            temp = heapq.heappop(heap)
            cost = temp[0]
            curr = temp[1]
            
            if curr in seen:
                continue
            total += cost
            for i in range(len(points)):
                if i not in seen:
                    distance = abs(points[curr][0] - points[i][0]) + abs(points[curr][1] - points[i][1])
                    heapq.heappush(heap, (distance, i))
                    seen.add(curr)
        return total