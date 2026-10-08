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
        q = deque([root])
        res = []
        while q:
            n = len(q)
            arr = []
            for i in range(n):
                temp = q.popleft()
                arr.append(temp)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            res.append(arr[len(arr) - 1].val)
        return res