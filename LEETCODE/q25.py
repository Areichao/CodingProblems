# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Time: O(2n) Space: O(1)
        dummy = pointer = ListNode(0, head)
        group_kth = None
        while pointer.next:
            group_tail = pointer.next
            group_kth = self.returnKthNode(pointer.next, k) # either kth value or none
            if not group_kth:
                break
            # if we have a group of k nodes at minimum, reverse the k elements
            self.reverseLinkedListSizeK(pointer.next, group_kth.next, k)
            # update pointer next to be new head
            pointer.next = group_kth
            # we want pointer to point to the tail of the current group
            pointer = group_tail 

        return dummy.next

    def reverseLinkedListSizeK(self, head: ListNode, prev_node: Optional[ListNode], k: int) -> None:
        """ given the head and size of linked list, k, and the previous node, reverse the linked list """
        # assumes we have atleast k elements in this list
        pointer = head
        for _ in range(k):
            orig_next = pointer.next
            pointer.next = prev_node
            prev_node = pointer 
            pointer = orig_next
    
    def returnKthNode(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """ given the head of a singly linked list, returns the kth node in a linked list if it exists (1 indexed)"""
        pointer = head
        for i in range(k - 1):
            if not pointer:
                break 
            pointer = pointer.next
        return pointer



