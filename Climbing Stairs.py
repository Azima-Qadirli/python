class Solution:
    def climbStairs(self, n: int) -> int:
        left = 0
        right = 1
        for i in range(n):
            left,right= right, left+right
        return right