class Solution:
    def inorderTraversal(self, root):
        result=[]
        def InOrder(node):
            if node is None:
                return
            InOrder(node.left)
            result.append(node.val)
            InOrder(node.right)
        
        
        InOrder(root)
        return result
