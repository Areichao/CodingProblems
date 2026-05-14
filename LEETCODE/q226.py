# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # just return if empty leaf
        if not root:
            return None
        
        # recursive case, return left and right 
        self.invertTree(root.left)
        self.invertTree(root.right)
    
        # swap two leaves of root
        left = root.left
        root.left = root.right
        root.right = left 

        # return root
        return root