'''class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]'''
'''class Solution:
    def rob(self, nums: list[int]) -> int:
        @cache
        def rec(i,amount):
            if i>=len(nums):
                return amount
            return max(rec(i+2,amount+nums[i]),rec(i+1,amount))
        return rec(0,0)'''
class Solution:
    def rob(self, nums:int) -> int:
        @cache
        def rec(i):
            if i<0:
                return 0
            if i==0:
                return nums[i]
            return max(rec(i-2)+nums[i],rec(i-1))
        return rec(len(nums)-1)
