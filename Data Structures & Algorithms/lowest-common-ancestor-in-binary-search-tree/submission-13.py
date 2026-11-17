# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        lt = self.lowestCommonAncestor(root.left, p, q)
        rt = self.lowestCommonAncestor(root.right, p, q)
        if rt and lt:
            return root
        return lt if lt else rt