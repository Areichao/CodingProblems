from typing import Optional
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """　木のノード　"""
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """ if root is the same, run bfs on left and right side """
        #　きのノードが両方ともからっぽだった時
        if not p and not q:
            return True
        # 一つ空っぽだった時期、あと木のノードが合わない時期
        elif (not p or not q) or (p.val != q.val):
            return False
        #　左と右両方見てみる
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    