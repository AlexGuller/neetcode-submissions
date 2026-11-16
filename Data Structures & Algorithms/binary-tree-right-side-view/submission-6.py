# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            qLen = len(q)
            while qLen > 0:
                currNode = q.popleft()
                lt = currNode.left
                rt = currNode.right
                if lt:
                    q.append(lt)
                if rt:
                    q.append(rt)
                if qLen == 1:
                    res.append(currNode.val)
                qLen -= 1
        return res