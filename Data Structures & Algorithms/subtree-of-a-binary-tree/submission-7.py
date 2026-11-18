# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2 or root1.val != root2.val:
                return False
            return isSame(root1.left, root2.left) and isSame(root1.right, root2.right)
        
        if not root and not subRoot:
            return True
        elif not root:
            return False
        q = collections.deque([root])
        while q:
            currNode = q.popleft()
            if isSame(currNode, subRoot):
                return True
            if currNode.left:
                q.append(currNode.left)
            if currNode.right:
                q.append(currNode.right)
        return False