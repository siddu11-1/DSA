class Solution(object):
    def numberOfSubarrays(self, nums, k):
        from collections import defaultdict

        count = defaultdict(int)
        count[0] = 1  # base case: zero odd numbers seen
        odd_count = 0
        result = 0

        for num in nums:
            if num % 2 == 1:
                odd_count += 1

            result += count[odd_count - k]
            count[odd_count] += 1

        return result