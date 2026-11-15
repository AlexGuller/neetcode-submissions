# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            lenQ = len(q)
            while lenQ > 1:
                temp = q.popleft()
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                lenQ -= 1
            val = q.popleft()
            res.append(val.val)
            if val.left:
                q.append(val.left)
            if val.right:
                q.append(val.right)
        return res