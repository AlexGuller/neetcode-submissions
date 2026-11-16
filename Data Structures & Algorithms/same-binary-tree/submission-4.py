# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qQ = deque([q])
        qP = deque([p])
        while qQ and qP:
            qNode = qQ.popleft()
            pNode = qP.popleft()
            if not pNode and not qNode:
                continue
            if (not pNode and qNode) or (not qNode and pNode) or (pNode.val != qNode.val):
                return False
            qLeft = qNode.left
            qRight = qNode.right
            pLeft = pNode.left
            pRight = pNode.right

            qQ.append(qLeft)
            qQ.append(qRight)
            qP.append(pLeft)
            qP.append(pRight)
        return True