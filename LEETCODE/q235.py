# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ yuh """
        # if one is equal to curr val, or they split off, return curr val
        if (root.val == p.val or root.val == q.val) or ((root.val > p.val or root.val > q.val) and (root.val < p.val or root.val < q.val)):
            return root
        # otherwise, if they both go left, check left
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # and same for right
        else:
            return self.lowestCommonAncestor(root.right, p, q)
