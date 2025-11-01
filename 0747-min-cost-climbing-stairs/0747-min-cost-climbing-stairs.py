class Solution(object):
    def minCostClimbingStairs(self, cost):
        prev2=prev1=0
        for c in cost:
            curr=c+min(prev1,prev2)
            prev2,prev1=prev1,curr
        return min(prev1,prev2)
        