# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: # if 0 or 1 elements in singly linked list, its false
            return False
        # can either do hash table to keep track of values or Floyd's Cycle Finding Algorithm
        slower = head
        faster = head.next
        while slower != faster:
            # if faster one reaches an end, no cycle
            if not faster or not faster.next:
                return False
            slower = slower.next
            faster = faster.next.next
        return True