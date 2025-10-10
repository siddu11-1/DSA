class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        total=0
        mi=float('inf')
        for right in range(len(nums)):
            total+=nums[right]
            while total>=target:
                mi=min(mi,right-left+1)
                total-=nums[left]
                left+=1
        return 0 if mi==float('inf') else mi