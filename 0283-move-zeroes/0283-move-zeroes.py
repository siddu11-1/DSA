class Solution(object):
    def moveZeroes(self, nums):
        last_non_zero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[last_non_zero],nums[i]=nums[i],nums[last_non_zero]
                last_non_zero+=1
        return nums
       
      
        