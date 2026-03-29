# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(0)
        pointer = head
        # while the head for either linked list still exists, add 2 values and carry over the carry, adding remainder into final output
        while l1 or l2: 
            # add the 2 values together
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            add = val1 + val2 + carry 
            remainder = add % 10 
            carry = add // 10
            pointer.next = ListNode(remainder)
            # iterate all lists
            pointer = pointer.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # both lists are gone, finish off carry now
        if carry:
            pointer.next = ListNode(carry)
        return head.next
