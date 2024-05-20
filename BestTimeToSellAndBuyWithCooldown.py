class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        ans = 0
        for i in prices:
            if buy > i:
                buy = i
            diff = i - buy
            if ans < diff:
                ans = diff
        return ans
