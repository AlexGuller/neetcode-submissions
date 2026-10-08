# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # identify all ancestors of p
        # identify all ancestors of q
        # compare and identify right before they differ
        pAncestors = []
        qAncestors = []
        def findAncestors(root, targetNode, arr):
            if not root:
                return False

            arr.append(root)

            if root is targetNode:
                return True

            if findAncestors(root.left, targetNode, arr) or findAncestors(root.right, targetNode, arr):
                return True
            
            arr.pop()
            return False
        findAncestors(root, p, pAncestors)
        findAncestors(root, q, qAncestors)
        comm = None
        i = 0
        while i < len(pAncestors) and i < len(qAncestors):
            if pAncestors[i] is not qAncestors[i]:
                break
            comm = pAncestors[i]
            i += 1
        return comm
