class Solution:
    def miceAndCheese(self, reward1: list[int], reward2: list[int], k: int) -> int:
        ans = sum(reward2)
        check = []
        for i in range (len(reward1)):
            check.append(reward1[i]-reward2[i])
        check.sort()
        while k:
            ans += check.pop()
            k-=1
        return ans

            


