# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = collections.deque([root])
        while q:
            qLen = len(q)
            while qLen > 0:
                currNode = q.popleft()
                if qLen == 1:
                    res.append(currNode.val)
                qLen -= 1
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
        return res