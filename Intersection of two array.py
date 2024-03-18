class Solution:
    def intersection(self, nums1:int, nums2: int):
        set_2 = set(nums2)
        response=[]
        for num in set_1:
            if num in set_2:
                response.append(num)
        return response