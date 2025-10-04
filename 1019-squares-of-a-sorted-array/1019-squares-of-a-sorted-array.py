class Solution(object):
    def sortedSquares(self, nums):
        l1=[]
        for i in range(len(nums)):
            nums[i]*=nums[i]
            l1.append(nums[i])
            l1.sort()
        return l1
        