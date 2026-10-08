class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total = 0
        visited = set()
        heap = [(0, 0)] # cost, idx -> cost first because want to connect to cheapest
        while len(visited) < len(points):
            cost, idx = heapq.heappop(heap)
            if idx in visited:
                continue
            visited.add(idx)
            total += cost
            for i in range(len(points)):
                if i not in visited:
                    heapq.heappush(heap, (abs(points[i][0] - points[idx][0]) + abs(points[i][1] - points[idx][1]), i))
        return total