class Solution(object):
    def resultsArray(self, nums, k):
        result=[]
        for i in range(len(nums)-k+1):
            window=nums[i:i+k]
            if all(window[j]+1==window[j+1] for j in range(k-1) ):
                result.append(max(window))
            else:
                result.append(-1)
        return result

        