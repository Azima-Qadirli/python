class Solution:
    def floodFill(self, image:int, sr: int, sc: int, color: int) -> int:
        if not image:
            return image
        
        def dfs(image, sr, sc, oldColor, newColor):
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != oldColor or image[sr][sc] == newColor:
                return
            
            image[sr][sc] = newColor
            dfs(image, sr + 1, sc, oldColor, newColor)
            dfs(image, sr - 1, sc, oldColor, newColor)
            dfs(image, sr, sc + 1, oldColor, newColor)
            dfs(image, sr, sc - 1, oldColor, newColor)
        
        oldColor = image[sr][sc]
        dfs(image, sr, sc, oldColor, color)
        return image
