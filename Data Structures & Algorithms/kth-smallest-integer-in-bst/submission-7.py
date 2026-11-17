# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.ans = None
        def inorder(root):
            if not root and not self.ans:
                return

            if root.left:
                inorder(root.left)

            self.count -= 1
            if self.count == 0:
                self.ans = root.val
                return
                
            if root.right:
                inorder(root.right)
            return
        inorder(root)
        return self.ans