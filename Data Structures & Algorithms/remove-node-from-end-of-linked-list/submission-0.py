# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse 
        # count n nodes
        p = None
        c = head
        while c:
            nx = c.next
            c.next = p
            p = c
            c = nx
        # => this gives us 

        dummy = ListNode(0,p)
        idx = dummy
        for _ in range(n-1):
            idx = idx.next
        idx.next = idx.next.next
        
        # reverse again
        p2 = None
        c2 = dummy.next
        while c2:
            nx2 = c2.next
            c2.next = p2
            p2 = c2
            c2 = nx2

        return p2