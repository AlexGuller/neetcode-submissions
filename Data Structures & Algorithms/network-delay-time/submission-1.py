class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # adjacency list
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        # make our minheap(time, vertice)
        minHeap = [(0, k)]
        # track the time we are at
        t = 0
        # set of vertices we visited
        visited = set()

        while minHeap:
            # retrieve weight of current and the node itself
            w1, n1 = heapq.heappop(minHeap)

            # check if we already visited the node
            if n1 in visited:
                continue

            # visit the node and set the time it took
            visited.add(n1)
            t = w1

            # look through all vertices on our heap and update their times
            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w2 + w1, n2))
        return t if len(visited) == n else -1
        