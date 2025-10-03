class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s - target) < abs(closest - target):
                    closest = s
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return target  # Exact match

        return closest