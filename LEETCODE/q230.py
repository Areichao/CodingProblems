# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def kth(root: Optional[TreeNode]) -> int:

            nonlocal k

            # base case
            if not root:
                return None
            
            # traverse left side
            left = kth(root.left)
            if left is not None:
                return left
            
            k -= 1
            if k == 0: # if k is 1 after left traversal, return val
                return root.val
            
            # traverse right side
            return kth(root.right)
        return kth(root)
