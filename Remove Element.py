class Solution:
    def removeElement(self, nums:int, val: int):
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index