# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root):
        if not root:
            return root
        
        def find(lnode,rnode,level):
            if not lnode and not rnode:
                return
            elif lnode and rnode and level % 2 == 0:
                lnode.val,rnode.val = rnode.val, lnode.val
            find(lnode.left,rnode.right,level+1)
            find(lnode.right,rnode.left,level+1)
        find(root.left,root.right,0)
        return root