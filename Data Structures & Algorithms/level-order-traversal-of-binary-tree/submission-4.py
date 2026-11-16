# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            currArr = []
            qLen = len(q)
            while qLen > 0:
                currNode = q.popleft()
                currArr.append(currNode.val)
                lt = currNode.left
                rt = currNode.right
                if lt:
                    q.append(lt)
                if rt:
                    q.append(rt)
                qLen -= 1
            res.append(currArr)
        return res