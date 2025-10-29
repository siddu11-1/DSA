class Solution(object):
    def maxArea(self, height):
        i=0
        j=len(height)-1
        re=0
        while i<j:
            re=max(re,(j-i)*min(height[i],height[j]))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return re

        