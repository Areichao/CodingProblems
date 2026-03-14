# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == val:
                curr.val = curr.next.val
                curr.next = curr.next.next
            else:
                curr = curr.next
        # if the last node in list is val, delete it. otherwise leave it be
        if curr.val == val:
            curr.val = None
        return head