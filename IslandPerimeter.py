'''class Solution:
    def islandPerimeter(self, grid:int) -> int:
        perimeter = 0
        rows = len(grid)
        cols=len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r>0 and grid[r-1][c] == 1:
                        perimeter -= 2
                    if c>0 and grid[r][c-1] == 1:
                        perimeter -= 2
        return perimeter'''
class Solution:
    def islandPerimeter(self, grid:int) -> int:
        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                return 1
            if grid[row][col] != 1:
                return 0
            grid[row][col] = 2  # Mark as visited
            
            perimeter = 0
            perimeter += dfs(row - 1, col)
            perimeter += dfs(row + 1, col)
            perimeter += dfs(row, col - 1)
            perimeter += dfs(row, col + 1)
            
            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0
