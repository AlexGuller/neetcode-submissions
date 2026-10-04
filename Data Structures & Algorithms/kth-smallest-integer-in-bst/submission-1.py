# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # dfs fully right then fully left to get smallest element at the end
        # then on the way back increment a counter that will return at count == k
        self.count = 0
        def dfs(root):
            if not root:
                return None
            
            result = dfs(root.left)
            if result is not None:
                return result
            
            self.count += 1
            if self.count == k:
                return root.val
            
            return dfs(root.right)

        return dfs(root)

        
        