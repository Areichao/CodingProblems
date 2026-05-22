# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def search(root: Optional[TreeNode], low: float, high: float):
            # if the root is none, return true
            if not root:
                return True
            # base case, if lower than low or higher than high, return false
            elif root.val <= low or root.val >= high:
                return False
            # otherwise, traverse left then right
            return search(root.left, low, root.val) and search(root.right, root.val, high)
        return search(root, float("-inf"), float("inf"))