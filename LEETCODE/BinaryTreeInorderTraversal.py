from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ return nodes in order from bottom depth first """
        elements = []
        # iterative approach?
        if not root.val:
            return []
        elif not root.left and not root.right:
            return [root.val]
        current_node = root.left
        while current_node:
            elements.insert(0, current_node.)
            current_node = current_node.left