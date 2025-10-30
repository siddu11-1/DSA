class Solution(object):
    def sortArrayByParity(self, nums):
        evens = [x for x in nums if x % 2 == 0]
        odds = [x for x in nums if x % 2 != 0]
        return evens + odds