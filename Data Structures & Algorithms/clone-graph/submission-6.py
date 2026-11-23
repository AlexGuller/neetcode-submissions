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
            return node
        # parent node
        newNode = Node(node.val, None)
        # hash {node val : neighbors}
        clones = {node: Node(node.val)}
        # queue to iterate neighbors
        q = collections.deque([node])
        # while we have things in queue
        while q:
            # get current node
            currNode = q.popleft()
            for nbr in currNode.neighbors:
                if nbr not in clones:
                    clones[nbr] = Node(nbr.val)
                    q.append(nbr)
                clones[currNode].neighbors.append(clones[nbr])
        return clones[node]