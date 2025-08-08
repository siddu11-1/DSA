"""class Solution(object):
    def countSubarrays(self, nums):
        ans=0
        for i in range(len(nums)-2):
            if nums[i]+nums[i+2]==2*nums[i+1]:
                ans+=1
        return ans"""
class Solution(object):
    def countSubarrays(self, nums):
       
        ans = 0
        for i in range(len(nums) - 2):
          
            if nums[i] + nums[i+2] == nums[i+1]/2.0:
                ans += 1
        return ans
               
               
                                           


        