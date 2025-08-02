'''class Solution(object):
    def maxSubArray(self, nums):
       maxsum=float('-inf')
       for i in range(len(nums)):

        
            for j in range(i+1,len(nums)+1):
                subarray=nums[i:j]
                currentsum=sum(subarray)
                if currentsum>maxsum:
                    maxsum=currentsum
       return maxsum
nums = list(map(int, input("Enter space-separated integers: ").split()))
sol = Solution()
print(sol.maxSubArray(nums))'''
class Solution(object):
    def maxSubArray(self, nums):
        max_current = max_global = nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            if max_current > max_global:
                max_global = max_current
        return max_global
        '''maxsum=float('-inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                subarray=nums[i:j]
                currentsum=sum(subarray)
                if currentsum>maxsum:
                    maxsum=currentsum
        return maxsum'''
                         
        


                
        