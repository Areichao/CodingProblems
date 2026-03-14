# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        starter = ListNode(-1)
        mergedList = starter

        while list1 and list2: # while both lists are non empty
            if list1.val <= list2.val:
                mergedList.next = list1
                list1 = list1.next
            else:
                mergedList.next = list2
                list2 = list2.next
            mergedList = mergedList.next
        
        # if one or other list is empty append rest of other list
        mergedList.next = list2 if not list1 else list1

        return starter.next
