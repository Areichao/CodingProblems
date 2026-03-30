"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # T: O(n) and S: O(n) hash table solution -> not interweaving method
        # first iterate through the linked list and save node values/copy into hash table
        if not head:
            return None
        
        ptr = head
        nodes = {}
        while ptr:
            nodes[ptr] = Node(ptr.val) # set next and random as none for now
            ptr = ptr.next
        
        # second iteration, create deep copy
        ptr = head
        while ptr:
            # set next and random values
            nodes[ptr].random = nodes.get(ptr.random)
            nodes[ptr].next = nodes.get(ptr.next)
            ptr = ptr.next

        return nodes[head]