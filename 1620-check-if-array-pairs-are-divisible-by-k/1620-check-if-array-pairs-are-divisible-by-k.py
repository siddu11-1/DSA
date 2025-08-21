class Solution(object):
    def canArrange(self, arr, k):
        from collections import Counter
        count = Counter()

        for num in arr:
            remainder = num % k
            count[remainder] += 1

        for r in count:
            if r == 0:
                if count[r] % 2 != 0:
                    return False
            elif k % 2 == 0 and r == k // 2:
                if count[r] % 2 != 0:
                    return False
            else:
                if count[r] != count[k - r]:
                    return False
        return True
            
       
        