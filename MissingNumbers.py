class Solution:
    def missingNumber(self, nums:int) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)