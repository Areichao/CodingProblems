# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """ iterative approach T: O(n) S: O(n)"""
        # base case 
        if not root:
            return []
        # loop setup
        queue = [root]
        result = []
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                level.append(node.val)
                # add to queue for left and right
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # add current level to the result
            result.append(level)
        return result