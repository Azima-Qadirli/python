class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True
        stack=[(root.left,root.right)]
        while stack:
            left,right = stack.pop()
            if left and right:
                if left.val !=right.val:
                    return False
                stack.append((left.left,right.right))        
                stack.append((left.right,right.left)) 
            elif left or right:
                return False
        return True
                       
'''def isMirror(left_node, right_node):
            if not left_node and not right_node:
                return True
            if not left_node or not right_node:
                return False
            return (left_node.val==right_node.val) and isMirror(left_node.left , right_node.right) and isMirror(left_node.right , right_node.left)
        if not root:
            return True
        return isMirror(root.left,root.right)'''
    
    