class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        check = [1, 1]
        while rowIndex >= 2:
            rowIndex -= 1
            newCheck = [1] * (len(check) + 1)
            for i in range(0, len(check) - 1):
                newCheck[i + 1] = check[i] + check[i + 1]
            check = newCheck
        return check