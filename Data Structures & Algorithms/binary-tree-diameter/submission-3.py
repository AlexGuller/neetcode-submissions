# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = 0
        def dfs(root):
            if not root:
                return 0
            lt = dfs(root.left)
            rt = dfs(root.right)
            self.maxDepth = max(self.maxDepth, lt + rt)
            return 1 + max(lt, rt)
        dfs(root)
        return self.maxDepth