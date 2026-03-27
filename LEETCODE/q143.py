# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # first we want to find the middle point of the singly linked list. we do this by using a slow and fast pointer.
        # if the fast pointer hits null or the .next value of the fast pointer is null, the middle point is the slow pointer
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # once we finish this loop, slow will be middle. split the list to be head -> slow (inc) and slow.next -> null
        # we will not save this but keep slow in mind as the last value of the first list

        # if the second list exists (that is, our list is 3 or greater), we will reverse it now
        pointer = slow.next
        prev = None
        while pointer:
            # reverse singly linked list
            temp_next = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = temp_next
        
        # split the list into 2 cleanly
        slow.next = None
        # once we reverse the second half of the list, we can merge one list into another by order
        l1 = head
        l2 = prev
        
        while l2: 
            # store next values for both lists
            next1 = l1.next
            next2 = l2.next

            # next value of l1 (the "list" we are modifying) becomes l2
            l1.next = l2
            
            # next value of list2 is next value of list1
            l2.next = next1

            # go next for both
            l1 = next1
            l2 = next2


        
        

            
