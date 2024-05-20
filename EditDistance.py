'''class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def find(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                return find(i + 1, j + 1)
            else:
                return 1 + min(find(i + 1, j + 1), find(i + 1, j), find(i, j + 1))
        return find(0, 0)'''
    
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        row,col=len(word1),len(word2)

        d = [[0]*(col+1)for _ in range(row+1)]
        for i in range (row+1):
            d[i][0] = i
        for j in range(col+1):
            d[0][j] = j
        for i in range (1,row+1):
            for j in range(1,col+1):

                d[i][j]=min(
                    d[i-1][j-1]+(0 if word1[i-1] == word2[j-1] else 1),
                    d[i][j-1] + 1,
                    d[i-1][j] + 1
                )
        return d[-1][-1]
    