# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        carry = 0
        while l1 or l2:
            # if we have a number for each
            if l1 and l2:
                n = l1.val + l2.val + carry
                carry = n // 10
                curr.next = ListNode(n % 10)
                curr = curr.next
                l1 = l1.next
                l2 = l2.next
            elif l1:
                n = l1.val + carry
                curr.next = ListNode(n % 10)
                carry = n // 10
                curr = curr.next
                l1 = l1.next
            else:
                n = l2.val + carry
                curr.next = ListNode(n % 10)
                carry = n // 10
                curr = curr.next
                l2 = l2.next
        if carry == 1:
            curr.next = ListNode(1)
        return res.next