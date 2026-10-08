class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        heap = [(0, 0)]
        total = 0
        while len(visited) < len(points):
            cost, curr = heapq.heappop(heap)
            if curr in visited:
                continue
            total += cost
            visited.add(curr)
            for i in range(len(points)):
                if i not in visited:
                    heapq.heappush(heap, (abs(points[curr][0] - points[i][0]) + abs(points[curr][1] - points[i][1]), i))
        return total