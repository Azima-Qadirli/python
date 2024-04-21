class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        def dfs(node,curSum):
            if not node:
                return False

            curSum += node.val
            if not node.left and not node.right:
                 return curSum == targetSum

            return(dfs(node.left,curSum)or dfs(node.right,curSum))

        return dfs(root,0)     
    
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False

        stack=[(root,0)]
        while stack:
            node,curSum=stack.pop()
            curSum+=node.val
            if not node.left and not node.right:
                if curSum == targetSum:
                    return True
            else:
                if  node.left:
                    stack.append((node.left,curSum))
                if  node.right:
                    stack.append((node.right,curSum))
        return False