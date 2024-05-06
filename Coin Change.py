from functools import cache

class Solution:
    def coinChange(self, coins: int, amount: int) -> int:
        @cache
        def rec(remaining):
            if remaining == 0:
                return 0

            numberOfCoins = float('inf')

            for coin in coins:
                if remaining - coin >= 0:
                    numberOfCoins = min(numberOfCoins, 1 + rec(remaining - coin))
            return numberOfCoins
        
        ans = rec(amount)
        return ans if ans < float('inf') else -1
