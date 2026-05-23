# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """ T: O(n), S: O(n)"""
        # base case
        if not root:
            return 0
        def maxTracker(root: TreeNode, maxValue: int) -> int:
            """ helper function """
            if not root:
                return 0
            elif root.val < maxValue:
                return maxTracker(root.left, maxValue) + maxTracker(root.right, maxValue)
            else:
                return 1 + maxTracker(root.left, root.val) + maxTracker(root.right, root.val)
        return maxTracker(root, root.val)