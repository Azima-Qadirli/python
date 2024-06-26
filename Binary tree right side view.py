# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level_size = len(queue)

            
            for i in range(level_size):
                node = queue[i]
                if i == level_size - 1:
                    result.append(node.val)

              
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            queue = queue[level_size:]

        return result


