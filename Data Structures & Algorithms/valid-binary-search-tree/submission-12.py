# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.check = True
        def dfs(low, high, root):
            if not root:
                return True
            if not (low < root.val < high):
                return False
            if not dfs(low, root.val, root.left) or not dfs(root.val, high, root.right):
                return False
            return True
        return dfs(float('-infinity'), float('infinity'), root)