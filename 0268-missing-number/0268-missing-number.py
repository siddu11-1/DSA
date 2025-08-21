class Solution(object):
    def missingNumber(self, arr):
        n = len(arr) + 1
        return n * (n - 1) // 2 - sum(arr)
