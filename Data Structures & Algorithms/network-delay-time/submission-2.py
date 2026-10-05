class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # adjacency matrix (vertice, weight)
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        # setup visited set
        visited = set()
        # setup minheap with initial start of weight 0
        minHeap = [(0, k)]
        # setup time to track where we are at
        t = 0

        # loop until nothing left in minheap
        while minHeap:
            # get node and weight of where we currently are
            w1, n1 = heapq.heappop(minHeap)

            # check that we havent already visited the node
            if n1 in visited:
                continue
            
            # visit the node and update our curr t
            visited.add(n1)
            t = w1

            # update all weights we can reach from this node
            for n2, w2 in adj[n1]:
                # if node hasnt been visited yet then we update its weight and put on heap
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        # return our current time we are at if we have visited each node
        return t if len(visited) == n else -1