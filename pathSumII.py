class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        def dfs(node,curSum,path,result):
            if not node:
                return
            curSum += node.val
            path.append(node.val)


            if not node.left and not node.right:
                if curSum == targetSum:
                    result.append(path[:])
            else:
                dfs(node.left,curSum,path,result)
                dfs(node.right,curSum,path,result)
            path.pop()
        
        result=[]
        dfs(root,0,[],result)
        return result

class Solution:
    def pathSum(self, root, targetSum: int) ->int:
        if not root:
            return []

        stack = [(root,0,[])]
        result=[]

        while stack:
            node,curSum,path=stack.pop()
            curSum += node.val
            path.append(node.val)

            if not node.left and not node.right:
                if curSum == targetSum:
                    result.append(path)
            else:
                if node.left:
                    stack.append((node.left,curSum,path[:]))
                if node.right:
                    stack.append((node.right,curSum,path[:]))
        return result
