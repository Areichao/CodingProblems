# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.value = 0 # keep track of current value

        def traverseGraph(node):
            if node is None: # (if node is not none)
                return 
            # go to the very bottom of right 
            traverseGraph(node.right)
            
            # add
            self.value += node.val
            node.val = self.value

            # visit left
            traverseGraph(node.left)
        
        traverseGraph(root)

        return root
