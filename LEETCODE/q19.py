# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # T: O(n) S: O(1)
        # dummy node start to account for edge case of n = len(linked list)
        dummy = ListNode(0, head)

        first = dummy
        second = dummy
        for _ in range(n): # get first pointer n steps ahead of other one (so that they will always be n steps apart)
            first = first.next
        while first.next: # once first pointer hits end, second will be 1 behind the nth from end
            first = first.next
            second = second.next
        # just skip the next one because it will be n
        second.next = second.next.next
        # return the new "head"
        return dummy.next