# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow.next
        slow.next = None
        rev = None
        while curr:
            temp = curr.next
            curr.next = rev
            rev = curr
            curr = temp
        
        hT = head
        while rev:
            temp1 = hT.next
            temp2 = rev.next

            hT.next = rev
            rev.next = temp1

            hT = temp1
            rev = temp2
        

