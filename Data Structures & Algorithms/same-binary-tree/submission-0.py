# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queueP = deque()
        queueQ = deque()
        queueP.append(p)
        queueQ.append(q)
        while queueP and queueQ:
            valP = queueP.popleft()
            valQ = queueQ.popleft()
            if not valP and not valQ:
                continue
            if not valP or not valQ or valP.val != valQ.val:
                return False
            queueP.append(valP.left)
            queueP.append(valP.right)
            queueQ.append(valQ.left)
            queueQ.append(valQ.right)
        return not queueQ and not queueP