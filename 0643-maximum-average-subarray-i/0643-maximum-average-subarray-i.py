class Solution(object):
    def findMaxAverage(self, nums, k):
        max_sum=curr_sum=sum(nums[:k])
        for i in range(k,len(nums)):
            curr_sum+=nums[i]-nums[i-k]
            max_sum=max(max_sum,curr_sum)
        return float(max_sum)/k


        