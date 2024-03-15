class Solution:
    def twoSum(self, numbers:int, target: int):
        i,j=0, len(numbers)-1
        while i<=j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1