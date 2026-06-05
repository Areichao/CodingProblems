# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # base case
        if not root:
            return []
        # add root as first queue value
        queue = [root]
        answer = []
        while queue:
            size = len(queue)
            answer.append(queue[0].val) # add the visible node to the answer
            for _ in range(size):
                node = queue.pop(0)
                # add right and then left subtrees into queue if they exist
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return answer
