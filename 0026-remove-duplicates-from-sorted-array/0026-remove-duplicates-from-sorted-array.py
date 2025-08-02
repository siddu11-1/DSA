'''class Solution(object):
    def removeDuplicates(self, nums):
        list1=[]
        for i in range(1,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    list1.append[i]
        return len(list1)  '''
class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)  # Remove the duplicate in-place
            else:
                i += 1
        return len(nums)        


        
        