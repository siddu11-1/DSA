class Solution(object):
    def rob(self, nums):
        def rob_linear(houses):
            prev1, prev2 = 0, 0
            for money in houses:
                temp = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = temp
            return prev1

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))