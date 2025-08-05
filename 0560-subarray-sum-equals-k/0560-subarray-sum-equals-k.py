
"""class Solution(object):
    def subarraySum(self, nums, k):
        result = []
        for i in range(len(nums)):
            for j in range( len(nums)):
                if nums[i] + nums[j] == k:
                    result.append([nums[i], nums[j]])
        return len(result)""" 
"""class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        for i in range(len(nums)):
            total=0
            for j in range(i,len(nums)):
                total+=nums[j]
                if total==k:
                    count+=1
        return count""" 
class Solution(object):
    def subarraySum(self, nums, k):
        from collections import defaultdict
        count = 0
        prefix_sum = 0
        freq = defaultdict(int)
        freq[0] = 1  # handles cases where prefix_sum itself equals k

        for num in nums:
            prefix_sum += num
            count += freq[prefix_sum - k]
            freq[prefix_sum] += 1

        return count                   
                                           
        