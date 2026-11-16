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
        def inorder(root):
            if not root or self.ans:
                return

            inorder(root.left)
            self.count -= 1
            if self.count == 0:
                self.ans = root.val
                return

            inorder(root.right)
        inorder(root)
        return self.ans
