class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        n=len(tasks)
        tasks.sort()
        processorTime.sort()
        j=n-1
        m=len(processorTime)
        ans=0
        for i in range(m):
            c=0
            while c<4 and j>=0:
                ans=max(ans,processorTime[i]+tasks[j])
                c+=1
                j-=1
        return ans

        