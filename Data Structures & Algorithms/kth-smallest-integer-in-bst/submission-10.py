# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.left = k
        self.ans = None
        def inorder(root):
            if not root or self.ans is not None:
                return
            inorder(root.left)
            if self.left == 1:
                self.ans = root.val
            self.left -= 1
            inorder(root.right)
            return
        inorder(root)
        return self.ans