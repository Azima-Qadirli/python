from collections import deque

class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        if not root:
            return []

        queue = deque()
        ans = []
        queue.append(root)
        while queue:
            level = []
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)  # Append left child, not node.val
                if node.right:
                    queue.append(node.right)  # Append right child, not node.val
            ans.append(level)
        return ans

