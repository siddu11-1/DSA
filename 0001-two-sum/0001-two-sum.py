class Solution:
    def twoSum(self, a, k):
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] + a[j] == k:
                    return [i, j]
        