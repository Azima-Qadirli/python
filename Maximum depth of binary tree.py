'''class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1'''

class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        l = self.maxDepth(root.left)        
        r = self.maxDepth(root.right)  

        return max(l,r)+1  
