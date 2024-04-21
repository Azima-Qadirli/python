'''class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        self.total = 0
        if not node:
            return 
        
        def dfs(node,left):
            dfs(node.left,True)
            dfs(node.right,False)
            
            if not node.left and not node.right and left:
                self.total += node.val
                
        dfs(root,False)
        return self.total'''
'''class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        ans = 0
        stack =[(root,False)]
        while stack:
            cur,is_Left = stack.pop()
            if not cur:
                continue
            if not cur.left and not cur.right:
                if is_Left:
                    ans += cur.val
            else:
                stack.append((cur.left,True))
                stack.append((cur.right,False))
        return ans'''
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)