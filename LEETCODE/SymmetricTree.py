from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(tree1: Optional[TreeNode], tree2:Optional[TreeNode]) -> bool:
            if not tree1 and not tree2:
                return True
            if (not tree1 or not tree2) or (tree1.val != tree2.val):
                return False
            return dfs(tree1.left, tree2.right) and dfs(tree1.right, tree2.left)
        return dfs(root.left, root.right)