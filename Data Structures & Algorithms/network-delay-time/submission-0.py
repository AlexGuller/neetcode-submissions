class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra's

        # create adjacency list
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        # initialize our minHeap with the initial start at k and time 0
        minHeap = [(0, k)]
        visit = set()
        t = 0

        # while our minheap has values in it
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            # if we already visited the node pass it
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            # loop through all edges of n1 as we just visited it and add it to our minheap with the time it took to get to n1 + the time it will take to get to n2
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w2 + w1, n2))
        return t if len(visit) == n else -1