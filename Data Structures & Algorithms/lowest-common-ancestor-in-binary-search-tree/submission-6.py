# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # iterate until we reach one of them
        def dfs(root, p, q) -> TreeNode:
            # iterate until we either reach p/q or None
            if not root or root is p or root is q:
                return root
            # search both sides until p/q or not found
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            # if we have a left and a right found then we found the root
            if left and right:
                return root
            # if we only have one of them, that means they are in the same branch
            return left or right
        return dfs(root, p, q)
