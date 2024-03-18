class Solution:
    def findKthLargest(self, nums:int, k: int) -> int:
        nums = sorted(nums)   
        return nums[len(nums)-k]
