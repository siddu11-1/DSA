from collections import Counter
class Solution(object):
    def deleteAndEarn(self, nums):
        if not nums: 
            return 0
        count=Counter(nums)
        max_num=max(nums)
        dp=[0]*(max_num+1)
        dp[0]=0
        dp[1]=count[1]*1
        for i in range(2,max_num+1):
            dp[i]=max(dp[i-1],dp[i-2]+count[i]*i)
        return dp[max_num]

        