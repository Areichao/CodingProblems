# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def longestPath(root: Optional[TreeNode]) -> int:
            """ Return longest path given the root """
            if not root:
                return 0
            left = longestPath(root.left)
            right = longestPath(root.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)
        longestPath(root)
        return self.diameter