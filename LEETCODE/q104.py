# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case, if node is empty
        if not root:
            return 0
        # recursive case
        # add 1 to whichever side of the tree is deeper
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))