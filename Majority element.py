class Solution:
    def majorityElement(self, nums:int) -> int:
        count,majority=0,None
#Iterate through each element in the input list
        for n in nums:
#if count becomes zero,update majority to the current element
            if count == 0:
                majority = n
# If maj is equal to the current element, increment count
                if majority == n:
                    count +=1
  # If maj is not equal to the current element, decrement count                   
                else:
                    count -= 1
        return majority
