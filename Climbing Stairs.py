class Solution:
    def climbStairs(self, n: int) -> int:
        left = 0  # Represents the number of ways to reach the current step with 1 step jump
        right = 1  # Represents the number of ways to reach the current step with 2 steps jump

        for i in range(n):
            left, right = right, left + right  # Update left and right using Fibonacci sequence relation

        return right  # Return the number of ways to reach the top step
