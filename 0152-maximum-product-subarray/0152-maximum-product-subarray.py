class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0

        max_prod = min_prod = result = nums[0]

        for num in nums[1:]:
            temp_max = max(num, max_prod * num, min_prod * num)
            temp_min = min(num, max_prod * num, min_prod * num)
            max_prod, min_prod = temp_max, temp_min
            result = max(result, max_prod)

        return result