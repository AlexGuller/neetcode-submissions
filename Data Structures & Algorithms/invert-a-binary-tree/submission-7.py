# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q = collections.deque([root])
        while q:
            currNode = q.popleft()
            lt = currNode.left
            currNode.left = currNode.right
            currNode.right = lt
            if currNode.right:
                q.append(currNode.right)
            if currNode.left:
                q.append(currNode.left)
        return root