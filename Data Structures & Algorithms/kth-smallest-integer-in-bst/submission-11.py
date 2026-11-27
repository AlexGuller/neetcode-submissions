# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = None
        self.count = k
        def dfs(root):
            if not root or self.ans:
                return
            dfs(root.left)
            if self.count == 1:
                self.ans = root.val
                self.count -= 1
                return
            self.count -= 1
            dfs(root.right)
            return
        dfs(root)
        return self.ans