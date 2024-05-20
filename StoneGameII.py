class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        @cache
        def play(i,m):
            s=sum(piles[i:])
            if i + 2 * m >= len(piles):
                return s
            return s - min(play(i+x,max(m,x))for x in range(1,2*m+1))
        return play(0,1)
