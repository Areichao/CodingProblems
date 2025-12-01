# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # base case
        if not root:
            return []
        # recursive case
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
    # iterative approach
   def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # a stack
        stack = []
        result = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result

        # morris traversal approach after, maybe
        