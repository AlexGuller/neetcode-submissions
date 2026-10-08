# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(rt, st):
            if rt and st:
                if rt.val != st.val:
                    return False
            elif not rt and not st:
                return True
            else:
                return False
            
            return True and sameTree(rt.left, st.left) and sameTree(rt.right, st.right)
        q = deque([root])
        while q:
            n = len(q)
            for i in range(n):
                temp = q.popleft()
                if sameTree(temp, subRoot):
                    return True
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        return False