class Solution(object):
    def climbStairs(self, n):
        if n<=2:
            return n
        prev1=1
        prev2=2
        x=0
        for i in range(2,n):
            x=prev1+prev2
            prev1=prev2
            prev2=x
        return x
        