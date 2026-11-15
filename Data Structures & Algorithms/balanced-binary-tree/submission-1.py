# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs down to last, check left height and right height at each level
        self.Bool = True
        def dfs(root):
            if not root:
                return 0
            lt = dfs(root.left)
            rt = dfs(root.right)
            if abs(rt - lt) > 1:
                self.Bool = False
            return 1 + max(lt, rt)
        dfs(root)
        return self.Bool