# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """ if root is the same, run DFS on left and right side """
        # time complexity is O(n) worse case, and space is O(n), O(logn) in the case of a balanced tree
        if not p and not q:
            return True
        elif (not p or not q) or (p.val != q.val):
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)