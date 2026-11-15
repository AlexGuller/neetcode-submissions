# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qP = deque([p])
        qQ = deque([q])
        while qP and qQ:
            tempQ = qQ.popleft()
            tempP = qP.popleft()
            if not tempP and not tempQ:
                continue
            if not tempP or not tempQ or tempQ.val != tempP.val:
                return False
            qP.append(tempP.left)
            qP.append(tempP.right)
            qQ.append(tempQ.left)
            qQ.append(tempQ.right)
        return len(qP) == len(qQ)