'''class Solution:
    def maxAreaOfIsland(self, grid:int) -> int:
        M,N=len(grid),len(grid[0])

        def dfs(r,c):
            if 0<=r<M and 0<=c<N and grid[r][c]==1:
                grid[r][c] = 0
                return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
            else:
                return 0
        output = 0
        for  r in range(M):
            for c in range(N):
                output = max(output,dfs(r,c))
        return output'''
'''class Solution:
    def maxAreaOfIsland(self, grid:int) -> int:
        def dfs(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
                return 0
            grid[i][j]=0
            area=1
            area += dfs(i+1,j)
            area += dfs(i-1,j)
            area += dfs(i,j+1)
            area += dfs(i,j-1)
            return area
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i,j))
        return max_area'''
class Solution:
    def maxAreaOfIsland(self, grid:int) -> int:
        def dfs(i, j):
            stack = [(i, j)]
            area = 0
            while stack:
                x, y = stack.pop()
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                    grid[x][y] = 0
                    area += 1
                    stack.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area