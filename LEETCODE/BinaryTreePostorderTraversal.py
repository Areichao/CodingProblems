# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        """ ノード、ノードの右と左側　"""
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    postorder = []
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Base case -> nothing above, root is gone
        if root is None:
            return self.postorder
        # Recursive case -> traverse left and right subtrees (left then right)

        # Traverse the left subtree
        self.postorderTraversal(root.left)

        # Traverse the right subtree 
        self.postorderTraversal(root.right)

        return self.postorder.append(root.val)

example1 = Solution()
tree = TreeNode(1,None,2,3)
print(example1.postorderTraversal([tree]))