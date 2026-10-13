# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(mx, root):
            if not root:
                return 0

            res = 0
            if root.val >= mx:
                res = 1
            mx = max(mx, root.val)
            res += dfs(mx, root.left)
            res += dfs(mx, root.right)
            return res
        return dfs(root.val, root)
            
