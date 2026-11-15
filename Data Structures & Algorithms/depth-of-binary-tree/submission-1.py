# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, currSize):
            if not root:
                return currSize
            maxLt = currSize + 1
            maxRt = currSize + 1
            if root.left:
                maxLt = dfs(root.left, currSize + 1)
            if root.right:
                maxRt = dfs(root.right, currSize + 1)
            return max(maxLt, maxRt)
        return dfs(root, 0)