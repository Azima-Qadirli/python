class Solution:
    def mergeTrees(self, root1, root2):
        stack1 = [root1]
        stack2 = [root2]
        if not root1:
            return root2

        while stack1:
            n1 = stack1.pop()
            n2 = stack2.pop()

            if n1 and n2:
                n1.val += n2.val
                if n2.left and not n1.left:
                    n1.left = TreeNode()
                if n2.right and not n1.right:
                    n1.right = TreeNode()
                stack1.append(n1.left)
                stack1.append(n1.right)
                stack2.append(n2.left)
                stack2.append(n2.right)
        return root1
class Solution:
    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1

        merged=TreeNode(root1.val + root2.val)
        merged.left=self.mergeTrees(root1.left,root2.left)
        merged.right=self.mergeTrees(root1.right,root2.right)
        return merged