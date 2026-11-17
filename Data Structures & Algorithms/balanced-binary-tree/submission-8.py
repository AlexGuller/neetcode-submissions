# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.boolVal = True
        def dfs(root):
            if not root or not self.boolVal:
                return 0
            lt = dfs(root.left)
            rt = dfs(root.right)
            if abs(lt - rt) > 1:
                self.boolVal = False
                return 0
            return 1 + max(lt , rt)
        dfs(root)
        return self.boolVal