"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # bfs 
        copies = {node: Node(node.val)}
        q = deque([node])
        while q:
            temp = q.popleft()
            for v in temp.neighbors:
                if v not in copies:
                    copies[v] = (Node(v.val))
                    q.append(v)
                copies[temp].neighbors.append(copies[v])
        return copies[node]