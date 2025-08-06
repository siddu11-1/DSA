"""class Solution(object):
    def trap(self, height):
        left,right=0,len(height)-1
        max_left=max_right=water=0
        while left<=right:
            if height[left]<height[right]: 
                
                if height[left]>=max_left:
                    
                    max_left=height[left]
                else:
                    water+=height[left]-max_left
                left+=1
            else:

                if height[right]>=max_right:
                    max_right=height[right]
                else:
                   water+=height[right]-max_right
                right-=1
        return water """
class Solution:
    def trap(self, height):
        left, right = 0, len(height) - 1
        max_left = max_right = water = 0
        while left <= right:
            if height[left] < height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    water += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    water += max_right - height[right]
                right -= 1
        return water



       
        