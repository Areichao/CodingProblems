# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # base case
        if not root:
            return True
        # recursive case (calculate max for left and right, then compare)
        left = self._maxDepth(root.left)
        right = self._maxDepth(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def _maxDepth(self, root: Optional[TreeNode]) -> int:
        """given a root, return the max depth"""
        # base case
        if not root:
            return 0
        # recursive case (1 + max depth)
        return 1 + max(self._maxDepth(root.left), self._maxDepth(root.right))